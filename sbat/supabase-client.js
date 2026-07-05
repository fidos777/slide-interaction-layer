// ===== Supabase — SATU sumber config (A2) =====
// Dikongsi oleh courseware-studio-shell.html + cair-decision-desk.html.
// Nilai url + anon diangkat dari cair-decision-desk.html (BUKAN nilai baru).
// JANGAN set storageKey/storage — biar default supaya localStorage key
// (sb-rlndyibqspcuhpgwlajl-auth-token) automatik dikongsi shell ⇄ desk.
// Muat @supabase/supabase-js@2 (CDN) SEBELUM fail ini.
(function () {
  var SB_URL = "https://rlndyibqspcuhpgwlajl.supabase.co";
  var SB_ANON = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJsbmR5aWJxc3BjdWhwZ3dsYWpsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI4MTkyMTAsImV4cCI6MjA5ODM5NTIxMH0.E1WPAL90Q-bldg7mP8GMtJkMfhHzfkm0YFMtRE0ewyE";
  if (!window.supabase || !window.supabase.createClient) {
    console.error("supabase-client.js: @supabase/supabase-js@2 belum dimuat sebelum fail ini.");
    return;
  }
  // Satu instance dikongsi. Default storage — jangan override.
  window.SB = window.SB || window.supabase.createClient(SB_URL, SB_ANON);
})();
