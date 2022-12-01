# Constructs
What are Constructs?
TODO: explain

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