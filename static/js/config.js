/**
 * Frontend Configuration
 * IMPORTANTE: En producción, configura estas variables en tu servidor
 */

// Obtener variables de entorno o usar valores por defecto
const SUPABASE_URL = window.ENV?.SUPABASE_URL || 'https://xapvvirzbxydmrymobja.supabase.co';
const SUPABASE_ANON_KEY = window.ENV?.SUPABASE_ANON_KEY || 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhhcHZ2aXJ6Ynh5ZG1yeW1vYmphIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTg4MTAwMjEsImV4cCI6MjA3NDM4NjAyMX0.1MPy5GIxJOHolm0Xl69bw8TN6h2F1PLaNt-d1CRsIV8';

export const config = {
  SUPABASE_URL,
  SUPABASE_ANON_KEY
};