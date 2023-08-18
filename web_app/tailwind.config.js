/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
      },
      colors: {
        black: '#111111',
        blue: '#00ADB5',
      },
      backgroundImage: () => ({
        'transparent-texture': "url('/src/img/earth_doodle.png')",
      })
    },
  },
  plugins: [],
}

