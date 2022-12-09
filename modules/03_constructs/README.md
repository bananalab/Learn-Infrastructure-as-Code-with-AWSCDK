# Constructs
What are Constructs?

Constructs are the basic building blocks of CDK apps. A construct represents a "cloud component" and encapsulates everything AWS CloudFormation needs to create the component.

## Create a simple Construct library

1. Generate a Construct project

```bash
mkdir my-construct && cd my-construct
npx projen new awscdk-construct --no-git
```

2. Build the project.

```bash
npx projen build
```

3. Enable Python build

```json
publishToPypi: {
    distName: 'rojopolis-my-construct',
    module: 'my-construct',
}
```