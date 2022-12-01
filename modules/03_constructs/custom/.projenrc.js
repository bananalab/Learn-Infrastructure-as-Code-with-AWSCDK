const { awscdk } = require('projen');
const project = new awscdk.AwsCdkConstructLibrary({
  author: 'Robert Jordan',
  authorAddress: '39421615+rojopolis@users.noreply.github.com',
  cdkVersion: '2.1.0',
  defaultReleaseBranch: 'main',
  name: 'custom',
  repositoryUrl: 'https://github.com/bananalab/Learn-Infrastructure-as-Code-with-AWSCDK.git',
  publishToPypi: {
    distName: 'rojopolis-custom-construct',
    module: 'custom',
  },
  // deps: [],                /* Runtime dependencies of this module. */
  // description: undefined,  /* The description is just a string that helps people understand the purpose of the package. */
  // devDeps: [],             /* Build dependencies for this module. */
  // packageName: undefined,  /* The "name" in package.json. */
});
project.synth();