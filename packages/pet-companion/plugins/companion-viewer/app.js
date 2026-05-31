(async function () {
  const params = new URLSearchParams(window.location.search);
  const bundlePath =
    params.get("bundle") ||
    "/repo/packages/pet-companion/examples/nori-public-case/runtime-adapters.json";
  const statePath =
    params.get("state") ||
    "/repo/packages/pet-companion/examples/nori-public-case/state/codex.example.json";

  const canvas = document.getElementById("pet-canvas");
  const context = canvas.getContext("2d");
  context.imageSmoothingEnabled = false;

  const nameNode = document.getElementById("pet-name");
  const descriptionNode = document.getElementById("pet-description");
  const runtimeNode = document.getElementById("runtime-name");
  const stateNode = document.getElementById("runtime-state");
  const resolvedNode = document.getElementById("resolved-state");
  const modeNode = document.getElementById("display-mode");
  const noteNode = document.getElementById("runtime-note");

  const bundle = await fetchJson(bundlePath);
  const image = await loadImage(resolveAsset(bundlePath, bundle.assets.spritesheet));
  const rows = bundle.atlas.rows;
  const fallbackOrder = bundle.state_contract.fallback_order;
  const cellWidth = bundle.atlas.cell_width;
  const cellHeight = bundle.atlas.cell_height;

  nameNode.textContent = bundle.pet.display_name || bundle.pet.id || "Pet Companion";
  descriptionNode.textContent = bundle.pet.description || "No description";
  modeNode.textContent = bundle.display_mode || "-";

  let frameIndex = 0;
  let activeState = "idle";
  let activeRow = rows.idle || firstRow(rows);

  function resolveRuntimeState(runtimeState) {
    const candidates = fallbackOrder[runtimeState] || [runtimeState, "idle"];
    for (const candidate of candidates) {
      if (rows[candidate] && rows[candidate].frames.length) {
        return { state: candidate, row: rows[candidate] };
      }
    }
    return { state: activeState, row: activeRow };
  }

  function renderFrame() {
    if (!activeRow || !activeRow.frames.length) {
      return;
    }
    const frameColumn = activeRow.frames[frameIndex % activeRow.frames.length];
    const sx = frameColumn * cellWidth;
    const sy = activeRow.row * cellHeight;
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.drawImage(
      image,
      sx,
      sy,
      cellWidth,
      cellHeight,
      0,
      0,
      canvas.width,
      canvas.height,
    );
    frameIndex = (frameIndex + 1) % activeRow.frames.length;
  }

  async function refreshState() {
    try {
      const state = await fetchJson(`${statePath}?t=${Date.now()}`);
      const resolved = resolveRuntimeState(state.state || "idle");
      activeState = resolved.state;
      activeRow = resolved.row;
      frameIndex = 0;
      runtimeNode.textContent = state.runtime || "-";
      stateNode.textContent = state.state || "idle";
      resolvedNode.textContent = activeState;
      noteNode.textContent = state.note || "-";
    } catch (error) {
      noteNode.textContent = `State read failed: ${error.message}`;
    }
  }

  setInterval(renderFrame, 180);
  setInterval(refreshState, 1500);

  await refreshState();
  renderFrame();
})();

function firstRow(rows) {
  const key = Object.keys(rows)[0];
  return rows[key];
}

async function fetchJson(path) {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText}`);
  }
  return response.json();
}

function loadImage(src) {
  return new Promise((resolve, reject) => {
    const image = new Image();
    image.onload = () => resolve(image);
    image.onerror = () => reject(new Error(`Failed to load image: ${src}`));
    image.src = src;
  });
}

function resolveAsset(bundlePath, relativePath) {
  return new URL(relativePath, new URL(bundlePath, window.location.href)).toString();
}
