<script setup lang="ts">
const props = defineProps<{ text: string }>();

type Block =
  | { kind: "paragraph"; html: string }
  | { kind: "list"; items: string[] }
  | { kind: "ordered-list"; items: string[] }
  | { kind: "table"; head: string[]; rows: string[][] };

function inline(value: string): string {
  const escaped = value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
  return escaped
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\[([^\]]+)]\((https?:\/\/[^\s)]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>')
    .replace(/(^|[^*])\*([^*\n]+)\*(?!\*)/g, "$1<em>$2</em>");
}

const blocks = computed<Block[]>(() => {
  const lines = props.text.replace(/\r/g, "").split("\n");
  const output: Block[] = [];
  let index = 0;

  while (index < lines.length) {
    if (!lines[index]?.trim()) {
      index += 1;
      continue;
    }

    if (lines[index]!.trim().startsWith("|") && lines[index + 1]?.includes("---")) {
      const cells = (line: string) => line.trim().replace(/^\||\|$/g, "").split("|").map((cell) => inline(cell.trim()));
      const head = cells(lines[index]!);
      index += 2;
      const rows: string[][] = [];
      while (index < lines.length && lines[index]!.trim().startsWith("|")) {
        rows.push(cells(lines[index]!));
        index += 1;
      }
      output.push({ kind: "table", head, rows });
      continue;
    }

    if (/^[-*]\s+/.test(lines[index]!.trim())) {
      const items: string[] = [];
      while (index < lines.length && /^[-*]\s+/.test(lines[index]!.trim())) {
        items.push(inline(lines[index]!.trim().replace(/^[-*]\s+/, "")));
        index += 1;
      }
      output.push({ kind: "list", items });
      continue;
    }

    if (/^\d+[.)]\s+/.test(lines[index]!.trim())) {
      const items: string[] = [];
      while (index < lines.length && /^\d+[.)]\s+/.test(lines[index]!.trim())) {
        items.push(inline(lines[index]!.trim().replace(/^\d+[.)]\s+/, "")));
        index += 1;
      }
      output.push({ kind: "ordered-list", items });
      continue;
    }

    const paragraph: string[] = [];
    while (
      index < lines.length
      && lines[index]!.trim()
      && !/^[-*]\s+/.test(lines[index]!.trim())
      && !/^\d+[.)]\s+/.test(lines[index]!.trim())
      && !(lines[index]!.trim().startsWith("|") && lines[index + 1]?.includes("---"))
    ) {
      paragraph.push(lines[index]!.trim());
      index += 1;
    }
    output.push({ kind: "paragraph", html: inline(paragraph.join(" ")) });
  }
  return output;
});
</script>

<template>
  <div class="xp-answer">
    <template v-for="(block, index) in blocks" :key="index">
      <p v-if="block.kind === 'paragraph'" v-html="block.html" />
      <ul v-else-if="block.kind === 'list'">
        <li v-for="(item, itemIndex) in block.items" :key="itemIndex" v-html="item" />
      </ul>
      <ol v-else-if="block.kind === 'ordered-list'">
        <li v-for="(item, itemIndex) in block.items" :key="itemIndex" v-html="item" />
      </ol>
      <div v-else class="xp-answer-table-wrap">
        <table>
          <thead><tr><th v-for="cell in block.head" :key="cell" v-html="cell" /></tr></thead>
          <tbody><tr v-for="(row, rowIndex) in block.rows" :key="rowIndex"><td v-for="(cell, cellIndex) in row" :key="cellIndex" v-html="cell" /></tr></tbody>
        </table>
      </div>
    </template>
  </div>
</template>

<style scoped>
.xp-answer { color: var(--ink-1); font-size: .95rem; line-height: 1.7; }
.xp-answer p { margin: 0 0 .8rem; }
.xp-answer p:last-child { margin-bottom: 0; }
.xp-answer ul, .xp-answer ol { margin: 0 0 .8rem; padding-left: 1.25rem; }
.xp-answer li { margin: .2rem 0; }
.xp-answer :deep(strong) { font-weight: 600; }
.xp-answer :deep(em) { font-style: italic; }
.xp-answer :deep(code) { padding: .08rem .28rem; border-radius: 4px; background: var(--sunk); font: .82em var(--font-num); }
.xp-answer :deep(a) { color: #1c5cab; text-decoration-thickness: 1px; text-underline-offset: 2px; }
.xp-answer-table-wrap { overflow-x: auto; margin: .15rem 0 .9rem; border: 1px solid var(--hairline); border-radius: 8px; }
.xp-answer table { width: 100%; border-collapse: collapse; font-size: .82rem; }
.xp-answer th, .xp-answer td { padding: .5rem .65rem; text-align: left; border-bottom: 1px solid var(--hairline); }
.xp-answer th { color: var(--ink-2); font-weight: 500; background: var(--sunk); }
.xp-answer tr:last-child td { border-bottom: 0; }
</style>
