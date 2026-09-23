import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://www.shstkv-digital.com",
  trailingSlash: "always",
  build: { format: "directory" },
  compressHTML: false
});
