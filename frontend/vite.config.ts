import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

const vasundharaEntryRoutes = {
  name: "vasundhara-entry-routes",
  configureServer(server: import("vite").ViteDevServer) {
    server.middlewares.use((req, _res, next) => {
      const pathname = (req.url || "/").split("?")[0];
      if (pathname === "/dashboard" || pathname === "/dashboard/") req.url = "/dashboard/index.html";
      next();
    });
  },
};

export default defineConfig({
  base: "./",
  plugins: [vasundharaEntryRoutes, react(), tailwindcss()],
  server: {
    port: 5173,
    proxy: { "/api": "http://127.0.0.1:8000" },
  },
  build: {
    rollupOptions: {
      input: {
        landing: "index.html",
        dashboard: "dashboard/index.html",
      },
      output: {
        manualChunks(id) {
          if (id.includes("node_modules")) {
            if (id.includes("recharts") || id.includes("d3-") || id.includes("victory-vendor")) {
              return "vendor-charts";
            }
            if (id.includes("leaflet")) {
              return "vendor-leaflet";
            }
          }
        },
      },
    },
  },
});
