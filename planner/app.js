"use strict";

const DATA_URL = "../analysis/data/sjw_talent_tree.json";
const EFFECT_DB_URL = "../analysis/data/sjw_effect_database.json";
const POINT_PROGRESS_URL = "../analysis/data/sjw_point_progression.json";
const RANK_LABELS = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"];
const NODE_FALLBACK_WIDTH = 184;
const NODE_FALLBACK_HEIGHT = 112;
const MIN_COLUMN_GAP = 34;
const MIN_ROW_GAP = 26;
const OFFSET_SCALE = 0.28;
const MAX_OFFSET_X = 22;
const MAX_OFFSET_Y = 10;
const POINT_CURRENCIES = ["SkillPoint", "WeaponPoint", "SpecialPoint", "IdentityPoint"];
const SYSTEM_LABELS = {
  class: "Classes",
  weapon: "Armes",
  jinwoo: "Sung Jinwoo",
  unattached: "Structures non rattachées",
};
const CURRENCY_LABELS = {
  SkillPoint: "Classe",
  WeaponPoint: "Arme",
  SpecialPoint: "Sung Jinwoo",
  IdentityPoint: "OverDrive",
};
const DEFAULT_BUDGETS = {};

const state = {
  model: null,
  effectDb: null,
  pointProgression: null,
  sections: [],
  nodeById: new Map(),
  activeSectionIndex: 0,
  activeSystem: "",
  activeSection: "",
  activeNodeId: null,
  selected: {},
  buildLevel: 75,
  limitToBuildLevel: true,
  budgets: { ...DEFAULT_BUDGETS },
  zoom: 1,
};

const els = {
  system: document.getElementById("systemSelect"),
  section: document.getElementById("sectionSelect"),
  budget: document.getElementById("budgetInput"),
  limitLevel: document.getElementById("levelLimitToggle"),
  notice: document.getElementById("notice"),
  viewport: document.getElementById("treeViewport"),
  canvas: document.getElementById("treeCanvas"),
  edgeLayer: document.getElementById("edgeLayer"),
  nodeLayer: document.getElementById("nodeLayer"),
  buildCount: document.getElementById("buildCount"),
  activeRank: document.getElementById("activeRank"),
  budgetSummary: document.getElementById("budgetSummary"),
  topLevelSummary: document.getElementById("topLevelSummary"),
  topSpentSummary: document.getElementById("topSpentSummary"),
  nodeDetails: document.getElementById("nodeDetails"),
  knownGains: document.getElementById("knownGains"),
  rawEffects: document.getElementById("rawEffects"),
  selectionList: document.getElementById("selectionList"),
  reset: document.getElementById("resetBuild"),
  share: document.getElementById("shareBuild"),
  export: document.getElementById("exportBuild"),
  import: document.getElementById("importBuild"),
  importFile: document.getElementById("importFile"),
  zoomIn: document.getElementById("zoomIn"),
  zoomOut: document.getElementById("zoomOut"),
  zoomReset: document.getElementById("zoomReset"),
};

function rankLabel(rank) {
  return RANK_LABELS[rank] || String(rank);
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function displayName(value) {
  return String(value ?? "").replaceAll("\\n", " ").replace(/\s+/g, " ").trim();
}

function rawIdList(value) {
  if (!value) return [];
  if (Array.isArray(value)) return value.map(String).filter(Boolean);
  return String(value).match(/\d+/g) || [];
}

function asArray(value) {
  return Array.isArray(value) ? value : [];
}

function clamp(value, min, max) {
  return Math.max(min, Math.min(max, value));
}

function minBuildLevel() {
  return state.pointProgression?.summary?.startLevel || 1;
}

function maxBuildLevel() {
  return state.pointProgression?.summary?.maxLevel || 75;
}

function progressionRowForLevel(level = state.buildLevel) {
  const rows = asArray(state.pointProgression?.levels);
  if (!rows.length) return null;
  const capped = clamp(Number(level) || minBuildLevel(), minBuildLevel(), maxBuildLevel());
  return rows.find((row) => Number(row.level) === capped) || rows.filter((row) => Number(row.level) <= capped).at(-1) || rows[0];
}

function identityBudgetForLevel(level = state.buildLevel) {
  const nodes = asArray(state.pointProgression?.identityOverdrive?.nodes);
  if (!nodes.length) return 0;
  const available = nodes.some((node) => {
    const required = Number(node.requiredLevel || node.chapterRequiredLevel || 0);
    return required <= 0 || Number(level) >= required;
  });
  return available ? 1 : 0;
}

function budgetsForLevel(level = state.buildLevel) {
  const row = progressionRowForLevel(level);
  const budgets = { ...(row?.cumulative || {}) };
  budgets.IdentityPoint = Math.max(Number(budgets.IdentityPoint || 0), identityBudgetForLevel(level));
  return budgets;
}

function currencyLabel(currency) {
  return CURRENCY_LABELS[currency] || currency;
}

function selectedRequiredNodeLevel(selected = state.selected) {
  return Object.keys(selected).reduce((required, nodeId) => {
    const node = state.nodeById.get(nodeId);
    return Math.max(required, nodeRequiredLevel(node));
  }, minBuildLevel());
}

function budgetCoversTotals(budgets, totals) {
  return Object.entries(totals || {}).every(([currency, spent]) => Number(budgets[currency] || 0) >= Number(spent || 0));
}

function requiredLevelForSelection(selected = state.selected) {
  const totals = selectedCostByCurrency(selected);
  const firstLevel = clamp(selectedRequiredNodeLevel(selected), minBuildLevel(), maxBuildLevel());
  for (let level = firstLevel; level <= maxBuildLevel(); level += 1) {
    if (budgetCoversTotals(budgetsForLevel(level), totals)) return level;
  }
  return null;
}

function budgetLevelForSelection(selected = state.selected) {
  if (state.limitToBuildLevel) return state.buildLevel;
  return requiredLevelForSelection(selected) || maxBuildLevel();
}

function budgetAnalysis(selected = state.selected) {
  const totals = selectedCostByCurrency(selected);
  const requiredLevel = requiredLevelForSelection(selected);
  const budgetLevel = state.limitToBuildLevel ? state.buildLevel : (requiredLevel || maxBuildLevel());
  const budgets = budgetsForLevel(budgetLevel);
  const currencies = [...new Set([...POINT_CURRENCIES, ...Object.keys(totals), ...Object.keys(budgets)])];
  return {
    totals,
    budgets,
    budgetLevel,
    requiredLevel,
    unreachable: !state.limitToBuildLevel && requiredLevel === null,
    currencies,
  };
}

function refreshBudgetsFromLevel() {
  state.buildLevel = clamp(Number(state.buildLevel) || maxBuildLevel(), minBuildLevel(), maxBuildLevel());
  state.budgets = budgetsForLevel(budgetLevelForSelection());
}

function parseOffset(raw) {
  if (!raw) return [0, 0, 0];
  const match = String(raw).match(/\[?\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*\]?/);
  return match ? [Number(match[1]), Number(match[2]), Number(match[3])] : [0, 0, 0];
}

function parseCost(rank) {
  if (!rank || rank.cost === "" || rank.cost === null || rank.cost === undefined) return null;
  const value = Number(rank.cost);
  return Number.isFinite(value) ? value : null;
}

function nodeCurrency(node) {
  return node.ranks.find((rank) => rank.pointCurrency)?.pointCurrency || "SkillPoint";
}

function rankCostLabel(rank, node) {
  const currency = rank?.pointCurrency || nodeCurrency(node);
  const cost = parseCost(rank);
  if (cost !== null) return `${cost} ${currency}`.trim();
  const raw = rank?.rawLevelUpCostValue ? `raw ${rank.rawLevelUpCostValue} ${currency}` : "";
  return raw ? `WIP (${raw})` : "WIP";
}

function emptyCostResult() {
  return { costs: {}, unknown: false };
}

function addCost(result, currency, value) {
  if (value === null) {
    result.unknown = true;
    return result;
  }
  result.costs[currency] = (result.costs[currency] || 0) + value;
  return result;
}

function mergeCostResults(...items) {
  const result = emptyCostResult();
  for (const item of items) {
    if (!item) continue;
    result.unknown = result.unknown || item.unknown;
    for (const [currency, value] of Object.entries(item.costs || {})) {
      result.costs[currency] = (result.costs[currency] || 0) + value;
    }
  }
  return result;
}

function costResultTotal(result) {
  return Object.values(result.costs || {}).reduce((sum, value) => sum + value, 0);
}

function formatCostResult(result) {
  const chunks = Object.entries(result.costs || {}).map(([currency, value]) => `${value} ${currency}`);
  if (result.unknown) chunks.push("WIP");
  return chunks.length ? chunks.join(" + ") : "0";
}

function formatSpentSummary(totals, unknownCosts = 0) {
  const entries = Object.entries(totals || {}).filter(([, value]) => value > 0);
  if (!entries.length && !unknownCosts) return "0";
  const chunks = entries.map(([currency, value]) => `${value} ${currencyLabel(currency)}`);
  if (unknownCosts) chunks.push(`${unknownCosts} WIP`);
  return chunks.join(" + ");
}

function formatRemainingSummary(budgets, totals) {
  const chunks = POINT_CURRENCIES.map((currency) => {
    const budget = Number(budgets[currency] || 0);
    const spent = Number(totals[currency] || 0);
    if (!budget && !spent && currency === "IdentityPoint") return "";
    const remaining = budget - spent;
    const value = remaining >= 0 ? remaining : `${Math.abs(remaining)} manquant`;
    return `${currencyLabel(currency)} ${value}`;
  }).filter(Boolean);
  return chunks.length ? chunks.join(" · ") : "0";
}

function cheapestCostResult(options) {
  const known = options.filter((item) => !item.unknown);
  const pool = known.length ? known : options;
  return pool.sort((a, b) => costResultTotal(a) - costResultTotal(b))[0] || emptyCostResult();
}

function missingCostToRank(node, targetRank = 1, selected = state.selected, visiting = new Set()) {
  if (!node || visiting.has(node.nodeId)) return { costs: {}, unknown: true };
  const current = Number(selected[node.nodeId] || 0);
  if (current >= targetRank) return emptyCostResult();
  const nextVisiting = new Set(visiting);
  nextVisiting.add(node.nodeId);

  const rankCosts = emptyCostResult();
  for (let index = current; index < targetRank; index += 1) {
    const rank = node.ranks[index];
    addCost(rankCosts, rank?.pointCurrency || nodeCurrency(node), parseCost(rank));
  }

  if (current > 0 || !node.parents.length || node.parents.some((parentId) => Number(selected[parentId] || 0) > 0)) {
    return rankCosts;
  }

  const parentOptions = node.parents
    .map((parentId) => state.nodeById.get(parentId))
    .filter(Boolean)
    .map((parent) => missingCostToRank(parent, 1, selected, nextVisiting));
  return mergeCostResults(cheapestCostResult(parentOptions), rankCosts);
}

function selectedRank(nodeId) {
  return Number(state.selected[nodeId] || 0);
}

function sectionNodes() {
  return activeSections().flatMap((section) => section.nodes || []);
}

function currentSection() {
  return activeSections()[0] || state.sections[state.activeSectionIndex];
}

function sectionUnlock(sectionName) {
  return state.pointProgression?.skillTreeUnlocks?.[sectionName] || null;
}

function sectionRequiredLevel(sectionName) {
  return Number(sectionUnlock(sectionName)?.requiredLevel || 0);
}

function nodeIdentityInfo(node) {
  return asArray(state.pointProgression?.identityOverdrive?.nodes).find((item) => String(item.nodeId) === String(node?.nodeId)) || null;
}

function nodeAccessRequiredLevel(node) {
  const identity = nodeIdentityInfo(node);
  if (identity) return Number(identity.requiredLevel || identity.chapterRequiredLevel || 0);
  const access = asArray(node?.ranks).map((rank) => rank.accessCondition).find(Boolean) || "";
  if (!access.startsWith("MainQuestChapter:")) return 0;
  const chapter = access.split(":", 2)[1];
  const match = asArray(state.pointProgression?.identityOverdrive?.nodes).find((item) => String(item.unlockValue) === chapter);
  return Number(match?.chapterRequiredLevel || 0);
}

function nodeSection(node) {
  return state.sections.find((section) => asArray(section.nodes).some((item) => item.nodeId === node?.nodeId)) || null;
}

function nodeRequiredLevel(node) {
  const section = nodeSection(node);
  return Math.max(sectionRequiredLevel(section?.section), nodeAccessRequiredLevel(node));
}

function levelSatisfied(node) {
  return !state.limitToBuildLevel || state.buildLevel >= nodeRequiredLevel(node);
}

function isOverdriveNode(node) {
  return node?.nodeType === "Identity" || nodeCurrency(node) === "IdentityPoint" || Boolean(nodeIdentityInfo(node));
}

function selectedOverdriveNodeId(exceptNodeId = "") {
  return Object.entries(state.selected).find(([nodeId, rank]) => {
    if (nodeId === exceptNodeId || Number(rank) <= 0) return false;
    return isOverdriveNode(state.nodeById.get(nodeId));
  })?.[0] || "";
}

function overdriveBlocked(node) {
  return isOverdriveNode(node) && Boolean(selectedOverdriveNodeId(node.nodeId)) && selectedRank(node.nodeId) === 0;
}

function levelLockText(node) {
  if (!state.limitToBuildLevel) return "";
  const required = nodeRequiredLevel(node);
  if (!required || state.buildLevel >= required) return "";
  const section = nodeSection(node);
  const unlock = sectionUnlock(section?.section);
  const source = unlock?.chapterTitle ? ` (${unlock.chapterTitle})` : "";
  return `Niveau ${required} requis${source}`;
}

function nodeRequiredLevelSource(node) {
  const identity = nodeIdentityInfo(node);
  if (identity) return identity.requiredLevelSource || "MainQuestChapter";
  const section = nodeSection(node);
  const unlock = sectionUnlock(section?.section);
  if (unlock?.requiredLevel) return "SubTabUnlockCondition";
  return "";
}

function nodeQuestText(node) {
  const identity = nodeIdentityInfo(node);
  if (!identity) return "";
  const missions = asArray(identity.missionTitles).filter(Boolean);
  const missionText = missions.length ? ` -> ${missions.join(" / ")}` : "";
  const chapter = identity.chapterTitle || `${identity.unlockType}:${identity.unlockValue}`;
  return `${chapter}${missionText}`;
}

function activeSections() {
  if (!state.activeSystem || !state.activeSection) return [];
  return state.sections.filter((item) => item.system === state.activeSystem && item.section === state.activeSection);
}

function nodeName(nodeId) {
  return displayName(state.nodeById.get(nodeId)?.name || nodeId);
}

function skillGroup(groupId) {
  return state.effectDb?.skillsByGroupId?.[String(groupId)] || null;
}

function buffById(buffId) {
  return state.effectDb?.buffsById?.[String(buffId)] || null;
}

function wipBadge(item) {
  return item?.wip ? `<span class="wip-badge">WIP</span>` : "";
}

function statLine(stat) {
  return `
    <li>
      <span>${escapeHtml(stat.label || stat.field || stat.type || "Stat")}</span>
      <strong>${escapeHtml(stat.display || stat.rawValue || "0")}</strong>
      ${wipBadge(stat)}
      <small>${escapeHtml(stat.field || stat.type || "")}</small>
    </li>`;
}

function compactSkillLine(skill) {
  if (!skill) return "";
  const stats = asArray(skill.stats)
    .filter((stat) => ["Cooldown", "DamAttCoeff", "EXGain", "MPCon", "PGGain", "CrashDam"].includes(stat.field))
    .map((stat) => `${stat.label}: ${stat.display}`)
    .join(" · ");
  return `${skill.name || skill.id}${stats ? ` — ${stats}` : ""}`;
}

function compactBuffLine(buff) {
  if (!buff) return "";
  const stats = [
    ...asArray(buff.addedStats).map((stat) => stat.display || `${stat.type} ${stat.rawValue}`),
    ...asArray(buff.specialStates).map((special) => special.display || special.type),
  ].filter(Boolean);
  const trigger = buff.trigger?.buffIds?.length ? ` -> ${buff.trigger.buffIds.join(", ")}` : "";
  return `${buff.name || buff.id}${stats.length ? ` — ${stats.join(" · ")}` : ""}${trigger}`;
}

function effectReferences(effect) {
  const buffIds = new Set();
  if (effect.buffId) buffIds.add(String(effect.buffId));
  for (const id of rawIdList(effect.rawValue)) {
    if (effect.effectType === "TriggeredBuff" || buffById(id)) buffIds.add(id);
  }
  return {
    skillGroupId: effect.abilityId || (effect.effectType === "ActiveSkillReference" ? effect.rawValue : ""),
    buffIds: [...buffIds],
  };
}

function resolvedEffectSummary(effect) {
  const refs = effectReferences(effect);
  if (refs.skillGroupId) {
    const group = skillGroup(refs.skillGroupId);
    const skill = group?.skills?.[0];
    if (skill) return `Compétence active: ${compactSkillLine(skill)}`;
  }
  const buffLines = refs.buffIds.map((id) => compactBuffLine(buffById(id))).filter(Boolean);
  if (buffLines.length) return buffLines.join("; ");
  const value = effect.marginalGain !== "NON DÉTERMINÉ"
    ? effect.marginalGain
    : effect.displayedValue || effect.rawValue || "WIP";
  return `${effect.effectType}: ${value}`;
}

function readableEffectSummary(effect) {
  return resolvedEffectSummary(effect)
    .replaceAll(" — ", "\n  ")
    .replaceAll(" · ", "\n  ")
    .replaceAll("; ", "\n");
}

function effectHasWip(effect) {
  const refs = effectReferences(effect);
  const group = refs.skillGroupId ? skillGroup(refs.skillGroupId) : null;
  if (group?.wip || asArray(group?.skills).some((skill) => skill.wip || asArray(skill.stats).some((stat) => stat.wip))) return true;
  if (refs.buffIds.some((id) => {
    const buff = buffById(id);
    return buff?.wip
      || asArray(buff?.addedStats).some((stat) => stat.wip)
      || asArray(buff?.specialStates).some((special) => special.wip)
      || buff?.trigger?.wip;
  })) return true;
  return effect.confidence === "NON DÉTERMINÉ"
    || effect.marginalGain === "NON DÉTERMINÉ"
    || effect.cumulativeGain === "NON DÉTERMINÉ";
}

function nodeTooltip(node) {
  const lines = [
    `${displayName(node.name)} (${node.nodeId})`,
    `${node.nodeType || "Talent"} · ${node.nodeMaxLevel} rang${node.nodeMaxLevel > 1 ? "s" : ""}`,
  ];
  const required = nodeRequiredLevel(node);
  if (required) {
    const locked = state.limitToBuildLevel && state.buildLevel < required;
    lines.push(`Niveau requis: ${required}${locked ? " (verrouillé)" : ""}`);
  }
  const quest = nodeQuestText(node);
  if (quest) lines.push(`Quête liée: ${quest}`);
  if (overdriveBlocked(node)) lines.push("OverDrive verrouillé: un autre OverDrive est déjà actif.");
  for (const rank of node.ranks || []) {
    lines.push(`Rang ${rankLabel(rank.rank)} · ${rankCostLabel(rank, node)}`);
    for (const effect of rank.effects || []) {
      lines.push(`- ${readableEffectSummary(effect)}`, "");
    }
  }
  lines.push("WIP: les valeurs brutes sont affichées même quand la conversion finale reste à valider.");
  return lines.join("\n");
}

function setNotice(message, tone = "info") {
  els.notice.textContent = message || "";
  els.notice.dataset.tone = tone;
  if (message) {
    window.clearTimeout(setNotice.timer);
    setNotice.timer = window.setTimeout(() => {
      els.notice.textContent = "";
    }, 2800);
  }
}

function buildPayload() {
  return {
    version: 2,
    buildLevel: state.buildLevel,
    limitToBuildLevel: state.limitToBuildLevel,
    selected: Object.fromEntries(Object.entries(state.selected).filter(([, rank]) => Number(rank) > 0)),
  };
}

function encodeBuild(payload) {
  const json = JSON.stringify(payload);
  const bytes = new TextEncoder().encode(json);
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary).replaceAll("+", "-").replaceAll("/", "_").replaceAll("=", "");
}

function decodeBuild(encoded) {
  const padded = encoded.replaceAll("-", "+").replaceAll("_", "/").padEnd(Math.ceil(encoded.length / 4) * 4, "=");
  const binary = atob(padded);
  const bytes = Uint8Array.from(binary, (char) => char.charCodeAt(0));
  return JSON.parse(new TextDecoder().decode(bytes));
}

function loadBuildFromHash() {
  const params = new URLSearchParams(window.location.hash.slice(1));
  const encoded = params.get("build");
  if (!encoded) return;
  try {
    applyBuild(decodeBuild(encoded));
    setNotice("Build importé depuis le lien.");
  } catch (error) {
    setNotice("Lien de build illisible.", "error");
  }
}

function applyBuild(payload) {
  state.buildLevel = clamp(Number(payload.buildLevel || payload.level || state.buildLevel), minBuildLevel(), maxBuildLevel());
  state.limitToBuildLevel = payload.limitToBuildLevel !== undefined ? Boolean(payload.limitToBuildLevel) : state.limitToBuildLevel;
  refreshBudgetsFromLevel();
  const next = {};
  for (const [nodeId, rank] of Object.entries(payload.selected || payload.nodes || {})) {
    const node = state.nodeById.get(nodeId);
    const value = Math.max(0, Math.min(Number(rank) || 0, node?.nodeMaxLevel || 0));
    if (node && value > 0) next[nodeId] = value;
  }
  state.selected = next;
  pruneInvalidSelections();
}

function populateFilters() {
  const systems = [...new Set(state.sections.map((section) => section.system))];
  if (!systems.includes(state.activeSystem)) {
    state.activeSystem = systems[0] || "";
  }
  els.system.innerHTML = systems
    .map((system) => `<option value="${escapeHtml(system)}">${escapeHtml(SYSTEM_LABELS[system] || system)}</option>`)
    .join("");
  els.system.value = state.activeSystem;
  populateSectionSelect();
}

function populateSectionSelect() {
  const system = state.activeSystem || els.system.value;
  const sections = [...new Set(state.sections.filter((section) => section.system === system).map((section) => section.section))];
  if (!sections.includes(state.activeSection)) {
    state.activeSection = sections[0] || "";
  }
  els.section.innerHTML = sections.map((name) => {
    const required = sectionRequiredLevel(name);
    const locked = state.limitToBuildLevel && required && state.buildLevel < required;
    const suffix = locked ? ` (niv. ${required})` : "";
    return `<option value="${escapeHtml(name)}">${escapeHtml(name + suffix)}</option>`;
  }).join("");
  els.section.value = state.activeSection;
  const nextIndex = state.sections.findIndex((section) => section.system === system && section.section === state.activeSection);
  state.activeSectionIndex = nextIndex >= 0 ? nextIndex : 0;
  updateBudgetInput();
}

function setActiveTree(system, section) {
  state.activeSystem = system;
  state.activeSection = section || "";
  populateFilters();
}

function activeCurrency() {
  const counts = new Map();
  for (const node of sectionNodes()) {
    for (const rank of node.ranks) {
      const currency = rank.pointCurrency || "SkillPoint";
      counts.set(currency, (counts.get(currency) || 0) + 1);
    }
  }
  return [...counts.entries()].sort((a, b) => b[1] - a[1])[0]?.[0] || "SkillPoint";
}

function updateBudgetInput() {
  els.budget.min = String(minBuildLevel());
  els.budget.max = String(maxBuildLevel());
  els.budget.value = state.buildLevel;
  els.budget.placeholder = String(maxBuildLevel());
  els.budget.parentElement.firstChild.textContent = "Niveau du build";
  els.budget.disabled = !state.limitToBuildLevel;
  els.limitLevel.checked = state.limitToBuildLevel;
  els.limitLevel.toggleAttribute("checked", state.limitToBuildLevel);
}

function selectedCostByCurrency(selected = state.selected) {
  const totals = {};
  for (const [nodeId, rankCount] of Object.entries(selected)) {
    const node = state.nodeById.get(nodeId);
    if (!node) continue;
    for (let index = 0; index < rankCount; index += 1) {
      const rank = node.ranks[index];
      const currency = rank?.pointCurrency || nodeCurrency(node);
      const cost = parseCost(rank);
      if (cost === null) continue;
      totals[currency] = (totals[currency] || 0) + cost;
    }
  }
  return totals;
}

function unlockSatisfied(node, selected = state.selected) {
  if (!node.parents.length) return true;
  if (node.parents.length === 1) return Number(selected[node.parents[0]] || 0) > 0;
  return node.parents.some((parentId) => Number(selected[parentId] || 0) > 0);
}

function parentConditionText(node) {
  if (!node.parents.length) return "Racine";
  const names = node.parents.map(nodeName).join(", ");
  if (node.parents.length === 1) return names;
  return `${names} (convergence: un chemin entrant accepté provisoirement, règle à confirmer)`;
}

function canAfford(node, nextRank) {
  if (!state.limitToBuildLevel) return true;
  const rank = node.ranks[nextRank - 1];
  if (parseCost(rank) === null) return true;
  const currency = rank?.pointCurrency || nodeCurrency(node);
  const preview = { ...state.selected, [node.nodeId]: nextRank };
  const total = selectedCostByCurrency(preview)[currency] || 0;
  const budget = Number(state.budgets[currency] || 0);
  return total <= budget;
}

function canIncrease(node) {
  const current = selectedRank(node.nodeId);
  return current < node.nodeMaxLevel
    && levelSatisfied(node)
    && !overdriveBlocked(node)
    && unlockSatisfied(node)
    && canAfford(node, current + 1);
}

function setNodeRank(nodeId, rank) {
  const node = state.nodeById.get(nodeId);
  if (!node) return;
  const nextRank = Math.max(0, Math.min(rank, node.nodeMaxLevel));
  if (nextRank > selectedRank(nodeId) && !levelSatisfied(node)) {
    setNotice(levelLockText(node), "error");
    return;
  }
  if (nextRank > selectedRank(nodeId) && overdriveBlocked(node)) {
    const active = state.nodeById.get(selectedOverdriveNodeId(nodeId));
    setNotice(`Un seul OverDrive peut être activé: ${displayName(active?.name || active?.nodeId)} est déjà sélectionné.`, "error");
    return;
  }
  if (nextRank > selectedRank(nodeId) && !unlockSatisfied(node)) {
    setNotice(`Lien entrant manquant: ${node.parents.map(nodeName).join(", ")}`, "error");
    return;
  }
  if (nextRank > selectedRank(nodeId) && !canAfford(node, nextRank)) {
    setNotice("Budget insuffisant pour ce rang.", "error");
    return;
  }
  if (nextRank > 0) state.selected[nodeId] = nextRank;
  else delete state.selected[nodeId];
  state.activeNodeId = nodeId;
  pruneInvalidSelections();
  render();
}

function pruneInvalidSelections() {
  let changed = true;
  while (changed) {
    changed = false;
    const activeOverdrive = selectedOverdriveNodeId();
    for (const nodeId of Object.keys(state.selected)) {
      const node = state.nodeById.get(nodeId);
      if (!node
        || (state.limitToBuildLevel && !levelSatisfied(node))
        || !unlockSatisfied(node)
        || (activeOverdrive && nodeId !== activeOverdrive && isOverdriveNode(node))) {
        delete state.selected[nodeId];
        changed = true;
      }
    }
  }
}

function increaseNode(nodeId) {
  const node = state.nodeById.get(nodeId);
  if (!node) return;
  setNodeRank(nodeId, selectedRank(nodeId) + 1);
}

function decreaseNode(nodeId) {
  setNodeRank(nodeId, selectedRank(nodeId) - 1);
}

function nodeSize(node, dimensions) {
  return dimensions?.get(node.nodeId) || { width: NODE_FALLBACK_WIDTH, height: NODE_FALLBACK_HEIGHT };
}

function logicalRange(values) {
  const min = Math.min(...values);
  const max = Math.max(...values);
  return Array.from({ length: max - min + 1 }, (_, index) => min + index);
}

function layoutNodes(nodes, originX, dimensions = null) {
  if (!nodes.length) return [];
  const rowHeights = new Map();
  const columnWidths = new Map();
  for (const node of nodes) {
    const row = Number(node.visual.row) || 1;
    const column = Number(node.visual.column) || 1;
    const size = nodeSize(node, dimensions);
    rowHeights.set(row, Math.max(rowHeights.get(row) || 0, size.height));
    columnWidths.set(column, Math.max(columnWidths.get(column) || 0, size.width));
  }

  const rows = logicalRange([...rowHeights.keys()]);
  const columns = logicalRange([...columnWidths.keys()]);
  const yByRow = new Map();
  const xByColumn = new Map();
  let yCursor = 74;
  for (const row of rows) {
    yByRow.set(row, yCursor);
    yCursor += (rowHeights.get(row) || 0) + MIN_ROW_GAP;
  }
  let xCursor = originX + 40;
  for (const column of columns) {
    xByColumn.set(column, xCursor);
    xCursor += (columnWidths.get(column) || NODE_FALLBACK_WIDTH) + MIN_COLUMN_GAP;
  }

  return nodes.map((node) => {
    const [offsetX, offsetY] = parseOffset(node.visual.offset);
    const row = Number(node.visual.row) || 1;
    const column = Number(node.visual.column) || 1;
    const nudgeX = clamp(offsetX * OFFSET_SCALE, -MAX_OFFSET_X, MAX_OFFSET_X);
    const nudgeY = clamp(offsetY * OFFSET_SCALE, -MAX_OFFSET_Y, MAX_OFFSET_Y);
    return {
      node,
      width: nodeSize(node, dimensions).width,
      height: nodeSize(node, dimensions).height,
      x: (xByColumn.get(column) || originX) + nudgeX,
      y: (yByRow.get(row) || 74) + nudgeY,
    };
  });
}

function layoutSections(sections, dimensions = null) {
  const layouts = [];
  const bands = [];
  let cursor = 24;
  for (const section of sections) {
    const local = layoutNodes(section.nodes || [], cursor, dimensions);
    const maxX = Math.max(...local.map((item) => item.x + item.width), cursor + 220);
    const maxY = Math.max(...local.map((item) => item.y + item.height), 520);
    bands.push({ section, x: cursor, width: maxX - cursor + 28, height: maxY + 30 });
    layouts.push(...local.map((item) => ({ ...item, section })));
    cursor = maxX + 72;
  }
  return { layouts, bands };
}

function nextCostLabel(node) {
  const current = selectedRank(node.nodeId);
  const levelLock = levelLockText(node);
  if (current === 0 && levelLock) return levelLock;
  if (current === 0 && overdriveBlocked(node)) {
    const active = state.nodeById.get(selectedOverdriveNodeId(node.nodeId));
    return `OverDrive déjà actif: ${displayName(active?.name || active?.nodeId)}`;
  }
  if (current >= node.nodeMaxLevel) return `${current}/${node.nodeMaxLevel} - MAX`;
  const nextRank = node.ranks[current];
  const cost = rankCostLabel(nextRank, node);
  if (current === 0 && !unlockSatisfied(node)) {
    const missing = missingCostToRank(node, 1);
    return `à investir : ${formatCostResult(missing)} (direct : ${cost})`;
  }
  if (node.nodeMaxLevel === 1) return current ? "1/1 - MAX" : `Coût : ${cost}`;
  return `${current}/${node.nodeMaxLevel} - prochain : ${cost}`;
}

function buildBranchHtml(bands) {
  return bands.map(({ section, x, width, height }) => `
    <section class="branch-band" style="left:${x}px; width:${width}px; height:${height}px">
      <div class="branch-title">${escapeHtml(section.branch)}${section.deduced ? " - libellé déduit" : ""}</div>
    </section>
  `).join("");
}

function buildNodeHtml(layout, mode = "") {
  return layout.map(({ node, x, y }) => {
    const rank = selectedRank(node.nodeId);
    const locked = !unlockSatisfied(node) || !levelSatisfied(node) || overdriveBlocked(node);
    const active = state.activeNodeId === node.nodeId;
    const currency = nodeCurrency(node);
    const selectedClass = rank > 0 ? "selected" : "";
    const activeClass = active ? "active" : "";
    const lockedClass = locked ? "locked" : "";
    const levelClass = !levelSatisfied(node) ? "level-locked" : "";
    const overdriveClass = overdriveBlocked(node) ? "overdrive-locked" : "";
    const measureClass = mode === "measure" ? "measure" : "";
    const tooltip = nodeTooltip(node);
    return `
      <article class="node-card ${selectedClass} ${activeClass} ${lockedClass} ${levelClass} ${overdriveClass} ${measureClass}" style="left:${x}px; top:${y}px" data-node-id="${escapeHtml(node.nodeId)}" data-tooltip="${escapeHtml(tooltip)}">
        <div>
          <div class="node-name">${escapeHtml(displayName(node.name))}</div>
          <div class="node-cost">${escapeHtml(nextCostLabel(node))}</div>
          <div class="node-meta">
            <span>${rank}/${node.nodeMaxLevel} rang</span>
            <span>${escapeHtml(currency)}</span>
          </div>
        </div>
        <div class="node-meta">
          <span>${escapeHtml(node.nodeId)}</span>
          ${node.ranks.some((rankItem) => asArray(rankItem.effects).some((effect) => effectHasWip(effect))) ? '<span class="wip-mini">WIP</span>' : ""}
          <span class="node-buttons">
            <button class="node-action" type="button" data-action="decrease" data-node-id="${escapeHtml(node.nodeId)}" ${rank === 0 ? "disabled" : ""} title="Retirer un rang">-</button>
            <button class="node-action" type="button" data-action="increase" data-node-id="${escapeHtml(node.nodeId)}" ${canIncrease(node) ? "" : "disabled"} title="Ajouter un rang">+</button>
          </span>
        </div>
      </article>`;
  }).join("");
}

function measureNodeCards() {
  const dimensions = new Map();
  for (const card of els.nodeLayer.querySelectorAll(".node-card")) {
    const rect = card.getBoundingClientRect();
    dimensions.set(card.dataset.nodeId, { width: rect.width, height: rect.height });
  }
  return dimensions;
}

function renderEdges(nodes, layout, width, height) {
  const pos = new Map(layout.map((item) => [item.node.nodeId, item]));
  els.edgeLayer.setAttribute("width", width);
  els.edgeLayer.setAttribute("height", height);
  els.edgeLayer.setAttribute("viewBox", `0 0 ${width} ${height}`);

  const edgePaths = [];
  for (const node of nodes) {
    const parentPos = pos.get(node.nodeId);
    if (!parentPos) continue;
    for (const childId of node.children) {
      const child = state.nodeById.get(childId);
      const childPos = pos.get(childId);
      if (!child || !childPos) continue;
      const x1 = parentPos.x + parentPos.width / 2;
      const y1 = parentPos.y + parentPos.height;
      const x2 = childPos.x + childPos.width / 2;
      const y2 = childPos.y;
      const mid = Math.max(34, Math.abs(y2 - y1) * 0.42);
      const status = selectedRank(node.nodeId) > 0 && selectedRank(childId) > 0
        ? "selected"
        : selectedRank(node.nodeId) > 0
          ? "available"
          : (child.parents.length && !unlockSatisfied(child)) || !levelSatisfied(child) || overdriveBlocked(child)
            ? "blocked"
            : "";
      edgePaths.push(`<path class="edge-path ${status}" d="M ${x1} ${y1} C ${x1} ${y1 + mid}, ${x2} ${y2 - mid}, ${x2} ${y2}"></path>`);
    }
  }
  els.edgeLayer.innerHTML = edgePaths.join("");
}

function renderTree() {
  const sections = activeSections();
  const nodes = sectionNodes();
  const measured = layoutSections(sections);
  els.nodeLayer.innerHTML = buildNodeHtml(measured.layouts, "measure");
  const dimensions = measureNodeCards();
  const { layouts: layout, bands } = layoutSections(sections, dimensions);
  const width = Math.max(760, ...bands.map((item) => item.x + item.width));
  const height = Math.max(520, ...bands.map((item) => item.height));
  els.canvas.style.width = `${width}px`;
  els.canvas.style.height = `${height}px`;
  els.canvas.style.transform = `scale(${state.zoom})`;
  els.nodeLayer.innerHTML = buildBranchHtml(bands) + buildNodeHtml(layout);
  renderEdges(nodes, layout, width, height);
}

function selectedEffects() {
  const effects = [];
  for (const [nodeId, rankCount] of Object.entries(state.selected)) {
    const node = state.nodeById.get(nodeId);
    if (!node) continue;
    for (const rank of node.ranks.slice(0, rankCount)) {
      for (const effect of rank.effects || []) {
        effects.push({ node, rank, effect });
      }
    }
  }
  return effects;
}

function parsePercent(value) {
  const text = String(value || "");
  const match = text.match(/(-?\d+(?:[.,]\d+)?)\s*%/);
  return match ? Number(match[1].replace(",", ".")) : null;
}

function renderSummary() {
  const selectedEntries = Object.entries(state.selected).filter(([, rank]) => Number(rank) > 0);
  els.buildCount.textContent = `${selectedEntries.length} talent${selectedEntries.length > 1 ? "s" : ""}`;
  const analysis = budgetAnalysis();
  const totals = analysis.totals;
  const currencies = analysis.currencies
    .filter((currency) => Number(analysis.budgets[currency] || 0) > 0 || Number(totals[currency] || 0) > 0 || POINT_CURRENCIES.includes(currency));
  const unknownCosts = selectedEntries.reduce((count, [nodeId, rankCount]) => {
    const node = state.nodeById.get(nodeId);
    if (!node) return count;
    return count + node.ranks.slice(0, rankCount).filter((rank) => parseCost(rank) === null).length;
  }, 0);
  const levelLabel = state.limitToBuildLevel ? "Niveau limite" : "Niveau requis";
  const levelValue = analysis.unreachable
    ? `> ${maxBuildLevel()}`
    : `${analysis.budgetLevel} / ${maxBuildLevel()}`;
  const modeText = state.limitToBuildLevel ? "Limité au niveau choisi" : "Calculé depuis les points dépensés";
  els.budgetSummary.innerHTML = `
    <div class="metric-row"><span>Mode</span><strong>${escapeHtml(modeText)}</strong></div>
    <div class="metric-row ${analysis.unreachable ? "over" : ""}"><span>${escapeHtml(levelLabel)}</span><strong>${escapeHtml(levelValue)}</strong></div>
  ` + currencies.map((currency) => {
    const spent = totals[currency] || 0;
    const budget = analysis.budgets[currency];
    const over = spent > Number(budget || 0);
    const delta = Number(budget || 0) - spent;
    const remaining = delta >= 0 ? `${delta} restant${delta > 1 ? "s" : ""}` : `${Math.abs(delta)} manquant${Math.abs(delta) > 1 ? "s" : ""}`;
    const label = `${spent} / ${budget || 0} (${remaining})`;
    return `<div class="metric-row ${over ? "over" : ""}"><span>${escapeHtml(currencyLabel(currency))}</span><strong>${escapeHtml(label)}</strong></div>`;
  }).join("") + (unknownCosts
    ? `<div class="metric-row"><span>Coûts WIP</span><strong>${unknownCosts} rang${unknownCosts > 1 ? "s" : ""}</strong></div>`
    : "");
  els.topLevelSummary.querySelector("span").textContent = levelLabel;
  els.topLevelSummary.querySelector("strong").textContent = analysis.unreachable ? `> ${maxBuildLevel()}` : String(analysis.budgetLevel);
  els.topSpentSummary.querySelector("strong").textContent = formatRemainingSummary(analysis.budgets, totals);

  const percentGroups = new Map();
  const rawRows = [];
  for (const { node, rank, effect } of selectedEffects()) {
    const gain = parsePercent(effect.marginalGain);
    if (gain !== null && effect.confidence !== "NON DÉTERMINÉ") {
      const key = `${effect.effectType}|${effect.unit || "%"}`;
      const item = percentGroups.get(key) || { label: effect.effectType, unit: effect.unit || "%", value: 0, rows: [] };
      item.value += gain;
      item.rows.push({ node, rank, gain, confidence: effect.confidence });
      percentGroups.set(key, item);
    } else {
      rawRows.push({ node, rank, effect });
    }
  }

  els.knownGains.innerHTML = percentGroups.size
    ? [...percentGroups.values()]
        .sort((a, b) => a.label.localeCompare(b.label, "fr"))
        .map((item) => `
          <div class="effect-group">
            <h3>${escapeHtml(item.label)}</h3>
            <ul>
              ${item.rows.map((row) => `<li>${escapeHtml(displayName(row.node.name))} ${rankLabel(row.rank.rank)}: +${row.gain.toLocaleString("fr-FR", { maximumFractionDigits: 2 })}% (${escapeHtml(row.confidence)})</li>`).join("")}
            </ul>
            <div class="formula-note">Somme arithmétique: +${item.value.toLocaleString("fr-FR", { maximumFractionDigits: 2 })}%. Stat finale réelle: WIP.</div>
          </div>`)
        .join("")
    : `<div class="empty-state">Aucun gain chiffré démontré dans la sélection.</div>`;

  els.rawEffects.innerHTML = rawRows.length
    ? rawRows.slice(0, 18).map(({ node, rank, effect }) => `
      <div class="effect-row">
        <strong>${escapeHtml(displayName(node.name))} ${rankLabel(rank.rank)}</strong>
        <span>${escapeHtml(resolvedEffectSummary(effect))} <em>(${escapeHtml(effect.effectType)} · raw ${escapeHtml(effect.rawValue || "WIP")})</em></span>
      </div>`).join("")
    : `<div class="empty-state">Aucune valeur brute non interprétée dans la sélection.</div>`;

  els.selectionList.innerHTML = selectedEntries.length
    ? selectedEntries
        .map(([nodeId, rank]) => ({ node: state.nodeById.get(nodeId), rank }))
        .filter((item) => item.node)
        .sort((a, b) => displayName(a.node.name).localeCompare(displayName(b.node.name), "fr"))
        .map(({ node, rank }) => `<button class="selection-row" type="button" data-node-id="${escapeHtml(node.nodeId)}"><strong>${escapeHtml(displayName(node.name))}</strong><span>${rank}/${node.nodeMaxLevel}</span></button>`)
        .join("")
    : `<div class="empty-state">Aucun talent sélectionné.</div>`;
}

function effectText(rank) {
  const effects = rank.effects || [];
  if (!effects.length) return "WIP";
  return effects.map((effect) => readableEffectSummary(effect)).join("\n\n");
}

function renderIdList(ids) {
  return ids.length ? ids.map((id) => `<code>${escapeHtml(id)}</code>`).join(" ") : `<span class="muted-text">aucun</span>`;
}

function renderBuffDetail(buffId, depth = 0, seen = new Set()) {
  const buff = buffById(buffId);
  if (!buff) {
    return `<div class="effect-detail nested-${depth}"><strong>BuffID <code>${escapeHtml(buffId)}</code></strong><span class="muted-text">Non résolu dans la BDD.</span></div>`;
  }
  if (seen.has(buffId)) {
    return `<div class="effect-detail nested-${depth}"><strong>BuffID <code>${escapeHtml(buffId)}</code></strong><span class="muted-text">Référence déjà affichée.</span></div>`;
  }
  const nextSeen = new Set(seen);
  nextSeen.add(buffId);
  const childIds = asArray(buff.trigger?.buffIds);
  return `
    <div class="effect-detail nested-${depth}">
      <div class="effect-detail-title">
        <strong>${escapeHtml(buff.name || `Buff ${buff.id}`)}</strong>
        <span>${wipBadge(buff)} <code>${escapeHtml(buff.id)}</code></span>
      </div>
      ${buff.description ? `<p>${escapeHtml(buff.description)}</p>` : ""}
      <div class="raw-grid">
        <span>Type</span><strong>${escapeHtml(buff.largeType || "WIP")}</strong>
        <span>Durée raw</span><strong>${escapeHtml(buff.durationRaw)}</strong>
        <span>Stacks</span><strong>${escapeHtml(buff.stackMaxCount)}</strong>
        <span>Groupe</span><strong>${escapeHtml(buff.groupId)}</strong>
      </div>
      ${asArray(buff.addedStats).length ? `<ul class="stat-list">${buff.addedStats.map(statLine).join("")}</ul>` : ""}
      ${asArray(buff.specialStates).length ? `<ul class="stat-list">${buff.specialStates.map(statLine).join("")}</ul>` : ""}
      ${buff.trigger ? `
        <div class="trigger-box">
          <strong>Déclenchement ${wipBadge(buff.trigger)}</strong>
          <span>Condition: ${escapeHtml(buff.trigger.condition || "WIP")}</span>
          <span>Ratio raw: ${escapeHtml(buff.trigger.ratioRaw)} · Cooldown raw: ${escapeHtml(buff.trigger.coolTimeRaw)}</span>
          <span>Buffs déclenchés: ${renderIdList(childIds)}</span>
        </div>
        ${childIds.map((id) => renderBuffDetail(id, depth + 1, nextSeen)).join("")}
      ` : ""}
    </div>`;
}

function renderSkillDetail(groupId) {
  const group = skillGroup(groupId);
  if (!group) return `<div class="effect-detail"><strong>SkillGroupID <code>${escapeHtml(groupId)}</code></strong><span class="muted-text">Non résolu dans la BDD.</span></div>`;
  const skill = group.skills?.[0];
  if (!skill) return "";
  return `
    <div class="effect-detail">
      <div class="effect-detail-title">
        <strong>${escapeHtml(skill.name || group.name || groupId)}</strong>
        <span>${wipBadge(skill)} <code>${escapeHtml(groupId)}</code></span>
      </div>
      ${skill.description ? `<p>${escapeHtml(skill.description)}</p>` : ""}
      <div class="raw-grid">
        <span>SkillID</span><strong>${escapeHtml(skill.id)}</strong>
        <span>BaseSkillInfoKey</span><strong>${escapeHtml(skill.baseSkillInfoKey)}</strong>
        <span>Type</span><strong>${escapeHtml(skill.type || "WIP")}</strong>
        <span>Prefab</span><strong>${escapeHtml(skill.prefab || "WIP")}</strong>
      </div>
      ${asArray(skill.stats).length ? `<ul class="stat-list">${skill.stats.map(statLine).join("")}</ul>` : ""}
      ${asArray(skill.relatedBuffIds).length ? `
        <div class="trigger-box">
          <strong>Buffs liés</strong>
          <span>${renderIdList(skill.relatedBuffIds)}</span>
        </div>
        ${skill.relatedBuffIds.map((id) => renderBuffDetail(id, 1)).join("")}
      ` : ""}
    </div>`;
}

function renderEffectDetail(rank, effect) {
  const refs = effectReferences(effect);
  return `
    <div class="effect-card">
      <div class="effect-detail-title">
        <strong>Rang ${rankLabel(rank.rank)} · ${escapeHtml(effect.effectType)}</strong>
        <span>${effectHasWip(effect) ? '<span class="wip-badge">WIP</span>' : ""}<code>raw ${escapeHtml(effect.rawValue || "WIP")}</code></span>
      </div>
      ${refs.skillGroupId ? renderSkillDetail(refs.skillGroupId) : ""}
      ${refs.buffIds.map((id) => renderBuffDetail(id)).join("")}
      ${!refs.skillGroupId && !refs.buffIds.length ? `<div class="effect-detail"><span>${escapeHtml(resolvedEffectSummary(effect))}</span></div>` : ""}
    </div>`;
}

function renderNodeDetails() {
  const node = state.nodeById.get(state.activeNodeId) || sectionNodes()[0];
  if (!node) {
    els.nodeDetails.innerHTML = `<div class="empty-state">Aucun arbre chargé.</div>`;
    els.activeRank.textContent = "-";
    return;
  }
  state.activeNodeId = node.nodeId;
  const rank = selectedRank(node.nodeId);
  els.activeRank.textContent = `${rank}/${node.nodeMaxLevel}`;
  const parents = parentConditionText(node);
  const children = node.children.length ? node.children.map(nodeName).join(", ") : "Aucun";
  const requiredLevel = nodeRequiredLevel(node);
  const levelSource = nodeRequiredLevelSource(node);
  const questText = nodeQuestText(node);
  const levelBlocked = state.limitToBuildLevel && state.buildLevel < requiredLevel;
  const levelStatus = requiredLevel
    ? `${requiredLevel}${levelBlocked ? " (verrouillé)" : ""}${levelSource ? ` · ${levelSource}` : ""}`
    : (isOverdriveNode(node) ? "Aucun niveau minimum explicite dans la quête liée" : "Aucun");
  const overdriveStatus = isOverdriveNode(node)
    ? (selectedOverdriveNodeId(node.nodeId)
      ? `Verrouillé par ${displayName(state.nodeById.get(selectedOverdriveNodeId(node.nodeId))?.name || selectedOverdriveNodeId(node.nodeId))}`
      : "Choix unique")
    : "";
  els.nodeDetails.innerHTML = `
    <div class="detail-title">
      <h3>${escapeHtml(displayName(node.name))}</h3>
      <span class="pill muted">${escapeHtml(node.nodeId)}</span>
    </div>
    <div class="rank-actions">
      <button class="rank-button" type="button" data-action="decrease" data-node-id="${escapeHtml(node.nodeId)}" ${rank === 0 ? "disabled" : ""}>-</button>
      <button class="rank-button" type="button" data-action="increase" data-node-id="${escapeHtml(node.nodeId)}" ${canIncrease(node) ? "" : "disabled"}>+</button>
    </div>
    <div class="metric-row"><span>Condition d'accès</span><strong>${escapeHtml(parents)}</strong></div>
    <div class="metric-row ${levelBlocked ? "over" : ""}"><span>Niveau requis</span><strong>${escapeHtml(levelStatus)}</strong></div>
    ${questText ? `<div class="metric-row"><span>Quête liée</span><strong>${escapeHtml(questText)}</strong></div>` : ""}
    ${overdriveStatus ? `<div class="metric-row ${overdriveBlocked(node) ? "over" : ""}"><span>OverDrive</span><strong>${escapeHtml(overdriveStatus)}</strong></div>` : ""}
    <div class="metric-row"><span>Débloque</span><strong>${escapeHtml(children)}</strong></div>
    <div class="metric-row"><span>Position</span><strong>R${escapeHtml(node.visual.row)} / C${escapeHtml(node.visual.column)}</strong></div>
    <table class="mini-table">
      <thead><tr><th>Rang</th><th>Coût</th><th>Effet</th></tr></thead>
      <tbody>
        ${node.ranks.map((item) => `
          <tr>
            <td>${rankLabel(item.rank)}</td>
            <td>${escapeHtml(rankCostLabel(item, node))}</td>
            <td>${escapeHtml(effectText(item))}</td>
          </tr>`).join("")}
      </tbody>
    </table>
    <div class="effect-detail-list">
      <h4>Détails bruts et WIP</h4>
      ${node.ranks.flatMap((item) => (item.effects || []).map((effect) => renderEffectDetail(item, effect))).join("")}
    </div>
  `;
}

function render() {
  refreshBudgetsFromLevel();
  updateBudgetInput();
  renderTree();
  renderNodeDetails();
  renderSummary();
}

function setupEvents() {
  els.system.addEventListener("change", () => {
    const firstSection = state.sections.find((section) => section.system === els.system.value);
    setActiveTree(els.system.value, firstSection?.section || "");
    state.activeNodeId = sectionNodes()[0]?.nodeId || null;
    render();
  });
  els.section.addEventListener("change", () => {
    setActiveTree(state.activeSystem, els.section.value);
    state.activeNodeId = sectionNodes()[0]?.nodeId || null;
    render();
  });
  els.budget.addEventListener("change", () => {
    state.buildLevel = clamp(Number(els.budget.value) || minBuildLevel(), minBuildLevel(), maxBuildLevel());
    refreshBudgetsFromLevel();
    pruneInvalidSelections();
    populateSectionSelect();
    render();
  });
  els.limitLevel.addEventListener("change", () => {
    state.limitToBuildLevel = els.limitLevel.checked;
    refreshBudgetsFromLevel();
    pruneInvalidSelections();
    populateSectionSelect();
    render();
  });
  els.nodeLayer.addEventListener("click", (event) => {
    const button = event.target.closest("button[data-action]");
    const card = event.target.closest("[data-node-id]");
    if (!card) return;
    const nodeId = card.dataset.nodeId;
    state.activeNodeId = nodeId;
    if (button?.dataset.action) {
      event.stopPropagation();
      if (button.dataset.action === "increase") increaseNode(nodeId);
      if (button.dataset.action === "decrease") decreaseNode(nodeId);
    } else {
      render();
    }
  });
  els.nodeDetails.addEventListener("click", (event) => {
    const button = event.target.closest("button[data-action]");
    if (!button) return;
    event.stopPropagation();
    if (button.dataset.action === "increase") increaseNode(button.dataset.nodeId);
    if (button.dataset.action === "decrease") decreaseNode(button.dataset.nodeId);
  });
  els.selectionList.addEventListener("click", (event) => {
    const row = event.target.closest("[data-node-id]");
    if (!row) return;
    state.activeNodeId = row.dataset.nodeId;
    const section = state.sections.find((item) => item.nodes.some((node) => node.nodeId === state.activeNodeId));
    if (section) setActiveTree(section.system, section.section);
    render();
  });
  els.reset.addEventListener("click", () => {
    state.selected = {};
    window.history.replaceState(null, "", window.location.pathname);
    render();
  });
  els.share.addEventListener("click", async () => {
    const url = new URL(window.location.href);
    url.hash = `build=${encodeBuild(buildPayload())}`;
    window.history.replaceState(null, "", url);
    try {
      await navigator.clipboard.writeText(url.toString());
      setNotice("Lien copié.");
    } catch (error) {
      setNotice("Lien généré dans la barre d'adresse.");
    }
  });
  els.export.addEventListener("click", () => {
    const blob = new Blob([JSON.stringify(buildPayload(), null, 2)], { type: "application/json" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "sjw-overdrive-build.json";
    link.click();
    URL.revokeObjectURL(link.href);
  });
  els.import.addEventListener("click", () => els.importFile.click());
  els.importFile.addEventListener("change", async () => {
    const file = els.importFile.files[0];
    if (!file) return;
    try {
      applyBuild(JSON.parse(await file.text()));
      setNotice("Build importé.");
      render();
    } catch (error) {
      setNotice("JSON de build invalide.", "error");
    } finally {
      els.importFile.value = "";
    }
  });
  els.zoomIn.addEventListener("click", () => {
    state.zoom = Math.min(1.6, state.zoom + 0.1);
    renderTree();
  });
  els.zoomOut.addEventListener("click", () => {
    state.zoom = Math.max(0.55, state.zoom - 0.1);
    renderTree();
  });
  els.zoomReset.addEventListener("click", () => {
    state.zoom = 1;
    renderTree();
  });
}

async function init() {
  try {
    const [treeResponse, effectResponse, pointResponse] = await Promise.all([fetch(DATA_URL), fetch(EFFECT_DB_URL), fetch(POINT_PROGRESS_URL)]);
    if (!treeResponse.ok) throw new Error(`HTTP ${treeResponse.status}`);
    if (!effectResponse.ok) throw new Error(`HTTP ${effectResponse.status}`);
    if (!pointResponse.ok) throw new Error(`HTTP ${pointResponse.status}`);
    state.model = await treeResponse.json();
    state.effectDb = await effectResponse.json();
    state.pointProgression = await pointResponse.json();
    state.sections = state.model.trees || [];
    for (const section of state.sections) {
      for (const node of section.nodes || []) state.nodeById.set(node.nodeId, node);
    }
    state.buildLevel = maxBuildLevel();
    refreshBudgetsFromLevel();
    const initial = state.sections[0];
    if (initial) {
      state.activeSystem = initial.system;
      state.activeSection = initial.section;
    }
    setupEvents();
    populateFilters();
    state.activeNodeId = sectionNodes()[0]?.nodeId || null;
    loadBuildFromHash();
    render();
  } catch (error) {
    els.notice.textContent = "Impossible de charger les données du planner depuis cette page.";
    els.nodeDetails.innerHTML = `<div class="empty-state">${escapeHtml(error.message)}</div>`;
  }
}

init();
