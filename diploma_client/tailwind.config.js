/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts}'],
  theme: {
    extend: {
      colors: {
        navbar: {
          main: '#262626',
          text: '#FFFFFF',
          colored: '#fdba74',
          exit: '#EF4444'
        },
        footer: {
          main: '#262626',
          heading: '#FFFFFF',
          content: '#a3a3a3',
          hover: '#fdba74',
          border: '#FFFFFF'
        },
        font: {
          colored: '#fdba74',
          main: '#FFFFFF'
        },
        background: {
          one: '#171717',
          two: '#262626',
          three: '#404040'
        },
        button: {
          main: '#fdba74',
          mainhover: '#fb923c',
          text: '#262626',
          cancel: '#ef4444',
          cancelhover: '#b91c1c',
        },
      },
      fontFamily: {
        great: ['Rhythm', 'serif'],
        main: ['Nunito', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
