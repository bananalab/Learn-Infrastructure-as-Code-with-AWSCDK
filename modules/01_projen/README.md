# Projen
Projen is a project generator created by the CDK team to quickly bootstrap CDK (and other) projects.

usage:

```bash
npx projen new
```

```bash
projen new [PROJECT-TYPE-NAME] [OPTIONS]

Creates a new projen project

Commands:
  projen new awscdk-app-java   AWS CDK app in Java.
  projen new awscdk-app-py     AWS CDK app in Python.
  projen new awscdk-app-ts     AWS CDK app in TypeScript.
  projen new awscdk-construct  AWS CDK construct library project.
  projen new cdk8s-app-py      CDK8s app in Python.
  projen new cdk8s-app-ts      CDK8s app in TypeScript.
  projen new cdk8s-construct   CDK8s construct library project.
  projen new cdktf-construct   CDKTF construct library project.
  projen new java              Java project.
  projen new jsii              Multi-language jsii library project.
  projen new nextjs            Next.js project without TypeScript.
  projen new nextjs-ts         Next.js project with TypeScript.
  projen new node              Node.js project.
  projen new project           Base project.
  projen new python            Python project.
  projen new react             React project without TypeScript.
  projen new react-ts          React project with TypeScript.
  projen new typescript        TypeScript project.
  projen new typescript-app    TypeScript app.

Positionals:
  PROJECT-TYPE-NAME  optional only when --from is used and there is a single project type in the external module  [string]

Options:
      --post      Run post-synthesis steps such as installing dependencies. Use --no-post to skip  [boolean] [default: true]
  -w, --watch     Keep running and resynthesize when projenrc changes  [boolean] [default: false]
      --debug     Debug logs  [boolean] [default: false]
      --rc        path to .projenrc.js file  [string] [default: "/workspaces/Learn-Infrastructure-as-Code-with-AWSCDK/.projenrc.js"]
      --help      Show help  [boolean]
      --synth     Synthesize after creating .projenrc.js  [boolean] [default: true]
      --comments  Include commented out options in .projenrc.js (use --no-comments to disable)  [boolean] [default: true]
  -f, --from      External jsii npm module to create project from. Supports any package spec supported by npm (such as "my-pack@^2.0")  [string]
      --git       Run `git init` and create an initial commit (use --no-git to disable)  [boolean] [default: true]

Examples:
  projen new awscdk-app-ts         Creates a new project of built-in type "awscdk-app-ts"
  projen new --from projen-vue@^2  Creates a new project from an external module "projen-vue" with the specified version
```

## Excercise
1. Create a Python CDK App

    ```bash
    # Create directory for the app
    mkdir app
    cd app

    # Generate the project
    npx projen new awscdk-app-py --no-git
    ```

2. Explore the project layout.
3. Deploy the project.

    ```bash
    source .env/bin/activate
    npx cdk deploy
    ```

3. Explore .projenrc.py
4. Rename the project directory.

    ```bash
    cd ..
    mv app my-app
    cd my-app
    ``` 

3. Deploy the project again.

    ```bash
    npx cdk deploy
    ```

4. Fix it by running `projen`