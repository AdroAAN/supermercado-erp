/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
    // agrega rutas a tus archivos Django y JS donde uses clases tailwind
  ],
  safelist: [
    'bg-yellow-400',
    'hover:bg-yellow-500',
    'focus:ring-yellow-300',
    'text-black',
    // ... otras clases ...
    'modal',
    'modal-content',
    'hidden'
  ],
  theme: {
    extend: {
      colors: {
        acento: '#a3e635',
        'acento-bg': '#166534',
        soft: '#2f2f2f',
        muted: '#bbb',
        'bg-dark': '#1e1e1e',
        'bg-main': '#252525',
      },
      fontFamily: {
        inter: ["'Inter'", 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        nav: '0 2px 6px rgba(0,0,0,0.8)',
        main: '0 8px 24px rgba(0,0,0,0.7)',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(-10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
      },
      animation: {
        fadeIn: 'fadeIn 0.4s ease forwards',
      },
      scrollbar: {
        DEFAULT: {
          thumb: '#a3e635',
          track: '#2f2f2f',
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'), // útil para estilos de formularios
    require('@tailwindcss/typography'), // para contenido con texto enriquecido
    require('tailwind-scrollbar'),
  ],
};
