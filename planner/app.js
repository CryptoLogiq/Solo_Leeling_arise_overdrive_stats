"use strict";

const DATA_URL = "../analysis/data/sjw_talent_tree.json";
const RANK_LABELS = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"];
const SYSTEM_LABELS = {
  class: "Classes",
  weapon: "Armes",
  jinwoo: "Sung Jinwoo",
  unattached: "Structures non rattachées",
};
const DEFAULT_BUDGETS = {};

const state = {
  model: null,
  sections: [],
  nodeById: new Map(),
  activeSectionIndex: 0,
  activeSystem: "",
  activeSection: "",
  activeNodeId: null,
  selected: {},
  budgets: { ...DEFAULT_BUDGETS },
  zoom: 1,
};

const els = {
  system: document.getElementById("systemSelect"),
  section: document.getElementById("sectionSelect"),
  budget: document.getElementById("budgetInput"),
  notice: document.getElementById("notice"),
  viewport: document.getElementById("treeViewport"),
  canvas: document.getElementById("treeCanvas"),
  edgeLayer: document.getElementById("edgeLayer"),
  nodeLayer: document.getElementById("nodeLayer"),
  buildCount: document.getElementById("buildCount"),
  activeRank: document.getElementById("activeRank"),
  budgetSummary: document.getElementById("budgetSummary"),
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

function parseOffset(raw) {
  if (!raw) return [0, 0, 0];
  const match = String(raw).match(/\[?\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*\]?/);
  return match ? [Number(match[1]), Number(match[2]), Number(match[3])] : [0, 0, 0];
}

function parseCost(rank) {
  const value = Number(rank?.cost || 0);
  return Number.isFinite(value) ? value : 0;
}

function nodeCurrency(node) {
  return node.ranks.find((rank) => rank.pointCurrency)?.pointCurrency || "SkillPoint";
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

function activeSections() {
  if (!state.activeSystem || !state.activeSection) return [];
  return state.sections.filter((item) => item.system === state.activeSystem && item.section === state.activeSection);
}

function nodeName(nodeId) {
  return displayName(state.nodeById.get(nodeId)?.name || nodeId);
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
    version: 1,
    selected: Object.fromEntries(Object.entries(state.selected).filter(([, rank]) => Number(rank) > 0)),
    budgets: state.budgets,
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
  const next = {};
  for (const [nodeId, rank] of Object.entries(payload.selected || payload.nodes || {})) {
    const node = state.nodeById.get(nodeId);
    const value = Math.max(0, Math.min(Number(rank) || 0, node?.nodeMaxLevel || 0));
    if (node && value > 0) next[nodeId] = value;
  }
  state.selected = next;
  state.budgets = { ...DEFAULT_BUDGETS, ...(payload.budgets || {}) };
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
  els.section.innerHTML = sections.map((name) => `<option value="${escapeHtml(name)}">${escapeHtml(name)}</option>`).join("");
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
  const currency = activeCurrency();
  els.budget.value = state.budgets[currency] ?? "";
  els.budget.placeholder = "illimité";
  els.budget.parentElement.firstChild.textContent = `Budget de simulation ${currency}`;
}

function selectedCostByCurrency(selected = state.selected) {
  const totals = {};
  for (const [nodeId, rankCount] of Object.entries(selected)) {
    const node = state.nodeById.get(nodeId);
    if (!node) continue;
    for (let index = 0; index < rankCount; index += 1) {
      const rank = node.ranks[index];
      const currency = rank?.pointCurrency || nodeCurrency(node);
      totals[currency] = (totals[currency] || 0) + parseCost(rank);
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
  const rank = node.ranks[nextRank - 1];
  const currency = rank?.pointCurrency || nodeCurrency(node);
  if (state.budgets[currency] === undefined || state.budgets[currency] === "") return true;
  const preview = { ...state.selected, [node.nodeId]: nextRank };
  const total = selectedCostByCurrency(preview)[currency] || 0;
  const budget = Number(state.budgets[currency]);
  return total <= budget;
}

function canIncrease(node) {
  const current = selectedRank(node.nodeId);
  return current < node.nodeMaxLevel && unlockSatisfied(node) && canAfford(node, current + 1);
}

function setNodeRank(nodeId, rank) {
  const node = state.nodeById.get(nodeId);
  if (!node) return;
  const nextRank = Math.max(0, Math.min(rank, node.nodeMaxLevel));
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
    for (const nodeId of Object.keys(state.selected)) {
      const node = state.nodeById.get(nodeId);
      if (!node || !unlockSatisfied(node)) {
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

function layoutNodes(nodes, originX) {
  if (!nodes.length) return [];
  const raw = nodes.map((node) => {
    const [offsetX, offsetY] = parseOffset(node.visual.offset);
    return {
      node,
      x: (Number(node.visual.column) - 1) * 190 + offsetX * 0.35 + 80,
      y: (Number(node.visual.row) - 1) * 124 + offsetY * 0.35 + 82,
    };
  });
  const minX = Math.min(...raw.map((item) => item.x));
  const minY = Math.min(...raw.map((item) => item.y));
  return raw.map((item) => ({
    ...item,
    x: item.x - minX + originX + 40,
    y: item.y - minY + 74,
  }));
}

function layoutSections(sections) {
  const layouts = [];
  const bands = [];
  let cursor = 24;
  for (const section of sections) {
    const local = layoutNodes(section.nodes || [], cursor);
    const maxX = Math.max(...local.map((item) => item.x + 204), cursor + 220);
    const maxY = Math.max(...local.map((item) => item.y + 120), 520);
    bands.push({ section, x: cursor, width: maxX - cursor + 28, height: maxY + 30 });
    layouts.push(...local.map((item) => ({ ...item, section })));
    cursor = maxX + 72;
  }
  return { layouts, bands };
}

function nextCostLabel(node) {
  const current = selectedRank(node.nodeId);
  if (current >= node.nodeMaxLevel) return `${current}/${node.nodeMaxLevel} - MAX`;
  const nextRank = node.ranks[current];
  const cost = `${nextRank?.cost || 0} ${nextRank?.pointCurrency || nodeCurrency(node)}`.trim();
  if (node.nodeMaxLevel === 1) return current ? "1/1 - MAX" : `Coût : ${cost}`;
  return `${current}/${node.nodeMaxLevel} - prochain : ${cost}`;
}

function renderTree() {
  const sections = activeSections();
  const nodes = sectionNodes();
  const { layouts: layout, bands } = layoutSections(sections);
  const pos = new Map(layout.map((item) => [item.node.nodeId, item]));
  const width = Math.max(760, ...bands.map((item) => item.x + item.width));
  const height = Math.max(520, ...bands.map((item) => item.height));
  els.canvas.style.width = `${width}px`;
  els.canvas.style.height = `${height}px`;
  els.canvas.style.transform = `scale(${state.zoom})`;
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
      const x1 = parentPos.x + 82;
      const y1 = parentPos.y + 78;
      const x2 = childPos.x + 82;
      const y2 = childPos.y;
      const mid = Math.max(34, Math.abs(y2 - y1) * 0.42);
      const status = selectedRank(node.nodeId) > 0 && selectedRank(childId) > 0
        ? "selected"
        : selectedRank(node.nodeId) > 0
          ? "available"
          : child.parents.length && !unlockSatisfied(child)
            ? "blocked"
            : "";
      edgePaths.push(`<path class="edge-path ${status}" d="M ${x1} ${y1} C ${x1} ${y1 + mid}, ${x2} ${y2 - mid}, ${x2} ${y2}"></path>`);
    }
  }
  els.edgeLayer.innerHTML = edgePaths.join("");

  const branchHtml = bands.map(({ section, x, width, height }) => `
    <section class="branch-band" style="left:${x}px; width:${width}px; height:${height}px">
      <div class="branch-title">${escapeHtml(section.branch)}${section.deduced ? " - libellé déduit" : ""}</div>
    </section>
  `).join("");
  const nodeHtml = layout.map(({ node, x, y }) => {
    const rank = selectedRank(node.nodeId);
    const locked = !unlockSatisfied(node);
    const active = state.activeNodeId === node.nodeId;
    const currency = nodeCurrency(node);
    const selectedClass = rank > 0 ? "selected" : "";
    const activeClass = active ? "active" : "";
    const lockedClass = locked ? "locked" : "";
    return `
      <article class="node-card ${selectedClass} ${activeClass} ${lockedClass}" style="left:${x}px; top:${y}px" data-node-id="${escapeHtml(node.nodeId)}">
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
          <span class="node-buttons">
            <button class="node-action" type="button" data-action="decrease" data-node-id="${escapeHtml(node.nodeId)}" ${rank === 0 ? "disabled" : ""} title="Retirer un rang">-</button>
            <button class="node-action" type="button" data-action="increase" data-node-id="${escapeHtml(node.nodeId)}" ${canIncrease(node) ? "" : "disabled"} title="Ajouter un rang">+</button>
          </span>
        </div>
      </article>`;
  }).join("");
  els.nodeLayer.innerHTML = branchHtml + nodeHtml;
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
  const totals = selectedCostByCurrency();
  const currencies = [...new Set([...Object.keys(totals), activeCurrency()])];
  els.budgetSummary.innerHTML = currencies.map((currency) => {
    const spent = totals[currency] || 0;
    const budget = state.budgets[currency];
    const hasBudget = budget !== undefined && budget !== "";
    const over = hasBudget && spent > Number(budget);
    const label = hasBudget ? `${spent} / ${budget}` : `${spent} dépensés`;
    return `<div class="metric-row ${over ? "over" : ""}"><span>${escapeHtml(currency)}</span><strong>${escapeHtml(label)}</strong></div>`;
  }).join("");

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
            <div class="formula-note">Somme arithmétique: +${item.value.toLocaleString("fr-FR", { maximumFractionDigits: 2 })}%. Stat finale réelle: NON DÉTERMINÉE.</div>
          </div>`)
        .join("")
    : `<div class="empty-state">Aucun gain chiffré démontré dans la sélection.</div>`;

  els.rawEffects.innerHTML = rawRows.length
    ? rawRows.slice(0, 18).map(({ node, rank, effect }) => `
      <div class="effect-row">
        <strong>${escapeHtml(displayName(node.name))} ${rankLabel(rank.rank)}</strong>
        <span>${escapeHtml(effect.effectType)}: ${escapeHtml(effect.displayedValue || effect.rawValue || "NON DÉTERMINÉ")}</span>
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
  if (!effects.length) return "NON DÉTERMINÉ";
  return effects.map((effect) => {
    const value = effect.marginalGain !== "NON DÉTERMINÉ"
      ? effect.marginalGain
      : effect.displayedValue || effect.rawValue || "NON DÉTERMINÉ";
    return `${effect.effectType}: ${value}`;
  }).join("; ");
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
    <div class="metric-row"><span>Débloque</span><strong>${escapeHtml(children)}</strong></div>
    <div class="metric-row"><span>Position</span><strong>R${escapeHtml(node.visual.row)} / C${escapeHtml(node.visual.column)}</strong></div>
    <table class="mini-table">
      <thead><tr><th>Rang</th><th>Coût</th><th>Effet</th></tr></thead>
      <tbody>
        ${node.ranks.map((item) => `
          <tr>
            <td>${rankLabel(item.rank)}</td>
            <td>${escapeHtml(item.cost || 0)} ${escapeHtml(item.pointCurrency || "")}</td>
            <td>${escapeHtml(effectText(item))}</td>
          </tr>`).join("")}
      </tbody>
    </table>
  `;
}

function render() {
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
    const currency = activeCurrency();
    if (els.budget.value === "") delete state.budgets[currency];
    else state.budgets[currency] = Math.max(0, Number(els.budget.value) || 0);
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
    const response = await fetch(DATA_URL);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    state.model = await response.json();
    state.sections = state.model.trees || [];
    for (const section of state.sections) {
      for (const node of section.nodes || []) state.nodeById.set(node.nodeId, node);
    }
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
    els.notice.textContent = "Impossible de charger analysis/data/sjw_talent_tree.json depuis cette page.";
    els.nodeDetails.innerHTML = `<div class="empty-state">${escapeHtml(error.message)}</div>`;
  }
}

init();
