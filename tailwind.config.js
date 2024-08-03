/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html',
    './components/**/*.html',
     "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {},
    fontFamily: {
      'sans': ['McLaren', 'sans-serif'],
      'body': ['Poppins', 'sans-serif'],
    }
  },
  plugins: [
    require('flowbite/plugin')
  ],
};
