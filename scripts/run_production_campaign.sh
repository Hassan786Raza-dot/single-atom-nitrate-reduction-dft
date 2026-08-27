#!/usr/bin/env bash
set -euo pipefail

# Execute on a suitably resourced workstation or cluster, not the constrained sandbox.
# The script preserves every attempt and never promotes results automatically.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON="${PYTHON:-$ROOT/.venv-gpaw/bin/python}"
MANIFEST="$ROOT/data/production_campaign_manifest.csv"
OUTROOT="${OUTROOT:-$ROOT/data/gpaw_production_campaign}"
CUTOFF="${CUTOFF:-350}"
KX="${KX:-3}"
KY="${KY:-3}"
KZ="${KZ:-1}"
FMAX="${FMAX:-0.03}"
STEPS="${STEPS:-200}"

if [[ ! -x "$PYTHON" ]]; then
  echo "ERROR: validated Python executable not found: $PYTHON" >&2
  exit 2
fi
if [[ ! -f "$MANIFEST" ]]; then
  echo "ERROR: production manifest not found: $MANIFEST" >&2
  exit 2
fi

mkdir -p "$OUTROOT"
export GPAW_SETUP_PATH="${GPAW_SETUP_PATH:-/usr/share/gpaw-setups}"

while IFS=, read -r campaign_id stage sac_id adsorbate support input_structure required_checks status; do
  [[ "$campaign_id" == "campaign_id" ]] && continue
  [[ "$stage" != "bare_SAC_optimisation" ]] && continue
  input="$ROOT/$input_structure"
  out="$OUTROOT/$campaign_id"
  mkdir -p "$out"
  {
    echo "campaign_id=$campaign_id"
    echo "stage=$stage"
    echo "sac_id=$sac_id"
    echo "input=$input"
    echo "cutoff_eV=$CUTOFF"
    echo "kmesh=${KX}x${KY}x${KZ}"
    echo "fmax_eV_per_A=$FMAX"
    echo "max_steps=$STEPS"
    echo "status=ATTEMPTED_NOT_YET_ACCEPTED"
  } > "$out/metadata.txt"
  "$PYTHON" "$ROOT/scripts/run_gpaw_sac.py" "$input" "$out" \
    --cutoff "$CUTOFF" --kmesh "$KX" "$KY" "$KZ" \
    --fmax "$FMAX" --steps "$STEPS" > "$out/runner_stdout.txt" 2>&1 || true
  echo "Completed attempt: $campaign_id; inspect $out before updating any acceptance field" >&2
done < "$MANIFEST"

echo "CAMPAIGN_ATTEMPTS_COMPLETE_NOT_ACCEPTED"
