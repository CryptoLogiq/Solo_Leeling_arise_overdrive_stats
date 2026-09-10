# Solo Leveling: ARISE OVERDRIVE - GameData read-only inventory

Run date: 2026-09-09

All reads were done from the game directories. Generated files are only under this
workspace's `analysis/` directory.

## Sources

- Main GameData:
  `/media/SSD_Evogames/SteamLibrary/steamapps/common/Solo Leveling/GameData`
- StreamingAssets GameData:
  `/media/SSD_Evogames/SteamLibrary/steamapps/common/Solo Leveling/Solo_Leveling_ARISE_OVERDRIVE_Data/StreamingAssets/GameData`
- Decoder repo found at:
  `/home/cryptologiq/SoloLevelingAR-SaveGameEditor`
- Decoder used:
  `/home/cryptologiq/SoloLevelingAR-SaveGameEditor/tools/gamedata_codec.py`

## Inventory

- Main GameData: 495 `.byte` files.
- StreamingAssets GameData: 485 `.byte` files.
- All inspected `.byte` files parsed successfully.
- Main inventory: `analysis/gamedata_inventory_main.json`
- Streaming inventory: `analysis/gamedata_inventory_streaming.json`
- Candidate table inventory, scored by table and column names:
  `analysis/candidate_tables_by_columns.tsv`

## Main vs StreamingAssets

SHA256 comparison summary:

- Same: 481 files.
- Different: 2 files.
- Main-only: 12 files.
- Streaming-only: 2 files.

Differences:

- Different: `ChComBuff.byte`, `ChComInfo.byte`.
- Main-only: `CharRaidReplica.byte`, `CharRaidReplicaSkill.byte`,
  `EntryPopup.byte`, `HunterScoutSJWCutScene.byte`, `RaidBlessGrade.byte`,
  `RaidDungeon.byte`, `RaidMain.byte`, `RaidPlayCount.byte`,
  `RaidReplica.byte`, `RaidReplicaLevel.byte`, `RaidReplicaTrait.byte`,
  `RaidReplicaTraitBuff.byte`.
- Streaming-only: `TextData_PS.byte`, `TextData_Xbox.byte`.

Detailed comparison:
`analysis/gamedata_compare_main_vs_streaming.json`

## Localization

`TextData.byte` has 57,285 rows and these language columns:

`Value`, `Value_eng`, `Value_jpn`, `Value_chn`, `Value_twn`, `Value_tha`,
`Value_idn`, `Value_fra`, `Value_ita`, `Value_deu`, `Value_esp`, `Value_prt`,
`Value_rus`, `Value_pol`, `Value_nld`, `Value_fil`, `Value_swe`, `Value_dan`,
`Value_nob`, `Value_msa`, `Value_tur`.

French localization is `Value_fra`, not `Value_fre` / `Value_fr`.

## High-value Tables

Stats and conversion:

- `ChComStatDesc`: 55 rows. Defines stat type, percent/stat display flag,
  base value, conversion constants, min/max, tooltip, and battle-power weight.
- `SysConst`: 1 row. Contains global constants such as
  `BattleConfig.PrecisionLevelConstValue`, `BattleConfig.DefRefConstant`,
  critical base values, battle-power correction constants, caps.
- `CharCommonLevelStat`: base/up curves for Attack, Armor, MHP, Precision,
  CriticalRes, CriticalDamRes by standard type and level.
- `ChStat`: character stat template ratios and calibrated stat link.
- `CharCalibratedStat`: calibrated stat mode values.
- `CharAbilityCorrection`: base stat rank/value to `DamRatio`.
- `CharPCStatAbility`, `CharHunterAbility`: SJW/hunter ability effects.

Skills:

- `ChPCSkill`: Sung Jinwoo skill groups, levels, costs, skill category refs.
- `ChPCSkillInfo`: Sung Jinwoo skill payload: cooldown, MP cost/gain, total
  damage, ATK/DEF/HP coefficients, buffs, skill detail text keys.
- `CHObjSkill`, `ChMonSkill`, `ChShadSkill`, `CharPetSkill`,
  `CharRaidReplicaSkill`: same pattern for object/monster/shadow/pet/raid
  skills.
- `CharHunterSkillCategoryLevel`: hunter category level costs.
- `CharPCSkillTreeNode`, `CharPCSkillTreelMainTab`,
  `CharPCSkillTreelSubTab`: SJW skill tree layout, unlock links, node costs,
  node values.
- `DimensionSkillTree`: dimension skill tree nodes, buff groups and costs.
- `ChComBuff`: buff stat additions, standards, duration, trigger data.

Enemies, stages, penalties, power correction:

- Stage-level columns appear across `AdventDungeon`, `InstanceDungeon`,
  `WorldContents`, `WorldBossAdvent`, `Tower`, `TimeAttack`, `RaidDungeon`,
  `DungeonTestStage`, etc.: `StageMonsterLevel`, `IngameStatLevel`,
  `StageMonsterSkillLevel`, `RecommendedPower`.
- `Penalty`, `PenaltyFix`, `PenaltyGroup`, `PenaltyLevel`: penalty metadata,
  target grade fields, buff/skill links, values.
- `BattlePowerCorretCondition`: level-indexed battle-power correction values.

Decoded JSON exports are in `analysis/decoded_tables/`.

## Stat Conversion Findings

Important constants from `SysConst`:

- `BattleConfig.PrecisionLevelConstValue = 50`
- `BattleConfig.DefRefConstant = 107`
- `BattleConfig.BaseCriChanceWeight = 500`
- `BattleConfig.BaseCriDamP = 3000`
- `BattleConfig.DamReduPLimitCap = 80`
- `BattleConfig.AttLimitCorrectionValue = 0.42`

`ChComStatDesc` key rows:

- `Critical`: `BaseValue=500`, `ConstValue=5000`, tooltip says the required
  value depends on target level.
- `CriDam`: `BaseValue=5000`, `ConstValue=5000`, same target-level wording.
- `Precision`: `BaseValue=5000`, `ConstValue=50`,
  `ConstLevelCondition=1`, `ConstLevelValue=50`.
- `Arm`: `ConstLevelCondition=1`, `ConstLevelValue=40`.
- `ArmPen`: `ConstValue=2000`, `ConstLevelCondition=60`,
  `ConstLevelValue=40`.
- `Dam`: `ConstValue=2000`, `ConstLevelCondition=60`,
  `ConstLevelValue=40`.

The strongest data-backed conversion candidate is:

`display_percent = BaseValue / 100 + rating / (rating + K) * 100`

This matches several supplied observations without forcing:

- `Critical 157 -> 8.04%`: using `BaseValue=5%`, `K=5000` gives `8.0444%`.
- `ArmPen 167 -> 7.71%`: using `K=2000` gives `7.7065%`.
- `Dam 74 -> 3.57%`: using `K=2000` gives `3.5680%`.

The other examples imply these effective `K` values:

- `Precision 117 -> 60.64%`: effective `K ~= 982.624`; nearest simple level
  constant is `K=1000` at level 21 if using `50 * (level - 1)`, giving
  `60.4745%`.
- `Arm 497 -> 35.42%`: effective `K ~= 906.162`; nearest `40 * (level - 1)`
  is `K=920` at level 24, giving `35.0741%`.
- `CriDam 140 -> 55.45%`: effective `K ~= 2428.807`; `SysConst`
  `BaseCriDamP=3000` gives `54.4586%`, while `ChComStatDesc.ConstValue=5000`
  gives `52.7237%`. This likely means the screenshot has an additional
  critical-damage percent source or uses a different context constant.

Detailed numeric probe:
`analysis/stat_conversion_probe.json`

## Skill Data Shape

`ChPCSkillInfo` is the main SJW coefficient table. Example columns:

- `Cooldown`, `MPCon`, `MPGain`, `TotalDamage`
- `DamAttCoeff`, `DamArmCoeff`, `DamMHPCoeff`
- `HealAttCoeff`, `HealArmCoeff`, `HealMHPCoeff`
- `BuffSet1..5`, `BoundBuffID`, `PassiveBuffID`
- `SkillDescDefalut`, `SkillDescDetail`, `SkillDescEnums`,
  `SkillDescBuffs`, `SkillDescLevel`

The generated flat skill summary is:
`analysis/skill_summary.tsv`

This is suitable for filtering by `SkillGroupID`, `SkillLevel`, cooldown,
resource cost, damage coefficient, and localized description.

## Limits of the Data-only Pass

The tables expose constants, levels, coefficients, buffs, caps, and many
relationships. They do not by themselves prove runtime operation order for all
multipliers, nor whether repeated identical buff effects are always additive or
multiplicative. For that, the next step would be a read-only code-symbol/string
pass over the game assemblies or IL2CPP metadata, plus controlled in-game
observations.
