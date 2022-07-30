module.exports = {
  extends: ['@commitlint/config-conventional'],

  rules: {
    // dependabot
    'header-max-length': [2, 'always', 200],
  },
};
