import { initialiseAnalytics } from "../utils/analytics";

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.hook("app:mounted", () => {
    initialiseAnalytics(useRouter());
  });
});
