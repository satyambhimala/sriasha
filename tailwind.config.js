/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html"
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "surface-tint": "#284b63",
        "on-background": "#181c1e",
        "tertiary-container": "#1d2e3b",
        "primary-fixed-dim": "#8daac4",
        "outline-variant": "#c4c6cf",
        "tertiary": "#1d2e3b",
        "surface": "#ffffff",
        "surface-container-high": "#cfcfcf",
        "primary": "#284b63",
        "surface-container-highest": "#c5c5c5",
        "on-surface-variant": "#43474e",
        "on-primary": "#ffffff",
        "surface-container-lowest": "#ffffff",
        "tertiary-fixed": "#b5b5b5",
        "surface-bright": "#ffffff",
        "inverse-surface": "#2d3133",
        "primary-container": "#3b5f7a",
        "inverse-on-surface": "#f1f1f1",
        "surface-container": "#b5b5b5",
        "secondary-container": "#cfcfcf",
        "on-tertiary": "#ffffff",
        "on-primary-container": "#ffffff",
        "primary-fixed": "#b7cbdc",
        "surface-dim": "#c5c5c5",
        "secondary-fixed-dim": "#cfcfcf",
        "surface-container-low": "#e3e3e3",
        "secondary-fixed": "#e3e3e3",
        "secondary": "#b5b5b5",
        "background": "#ffffff",
        "surface-variant": "#b5b5b5",
        "inverse-primary": "#8daac4",
        "on-secondary": "#181c1e",
        "outline": "#74777f",
        "on-secondary-container": "#181c1e",
        "on-surface": "#181c1e"
      },
      fontFamily: {
        "headline": ["Josefin Sans", "sans-serif"],
        "body": ["Barlow", "sans-serif"],
        "label": ["Barlow Condensed", "sans-serif"]
      },
      borderRadius: {
        "DEFAULT": "0.125rem",
        "lg": "0.25rem",
        "xl": "0.5rem",
        "full": "0.75rem"
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/container-queries'),
  ],
}
