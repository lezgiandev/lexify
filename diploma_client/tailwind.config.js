/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts}'],
  theme: {
    extend: {
      colors: {
        goldlight: '#fdba74',
        golddark: '#fb923c',
        darkone: '#1c1917',
        darktwo: '#292524',
        darkthree: '#44403c',
        darkfour: '#57534e',
        redlight: '#ef4444',
        reddark: '#b91c1c',
        greenlight: '#22c55e',
        light: '#ffffff'
      },
      fontFamily: {
        great: ['FleurDeLeah', 'serif'],
        main: ['Nunito', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
