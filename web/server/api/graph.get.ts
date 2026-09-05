export default defineEventHandler((event) => {
  setHeader(event, "Cache-Control", "public, max-age=300, stale-while-revalidate=3600");
  return getResearchGraph();
});
