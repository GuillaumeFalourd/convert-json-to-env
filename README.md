# Convert JSON to ENV

☞ Github Actions to convert variables from a JSON file to workflow ENV variables :octocat:

_**Note**: This action is supported on **all runners** operating systems (`ubuntu`, `macos`, `windows`)_

## 📚 Usage

### ⚠️ Requirements

- The [`actions/checkout`](https://github.com/marketplace/actions/checkout) is mandatory to use this action, as it will be necessary to access the JSON file.

- The `JSON` file currently only support one level variables. The **keys** will also be converted to UPPERCASE.

### Example

```yaml
    steps:
      - uses: actions/checkout@v2.3.4
      - uses: GuillaumeFalourd/convert-json-to-env@v1
        with:
          json_file: ./config.json
      - run: echo ${{ env.KEY1 }} #where "key1" is set on the config.json file
```

### ▶️ Action Inputs

Field | Mandatory | Default Value | Observation
------------ | ------------  | ------------- | -------------
**json_file** | YES | N/A | Path to JSON file <br/> _e.g: `./config.json` (when on root)_



## 🤝 Contributing

☞ If you're interested in contributing to this repository, please follow the [guidelines](https://github.com/GuillaumeFalourd/convert-json-to-env/blob/main/CONTRIBUTING.md)

## 🏅 Licensed

☞ This repository uses the [Apache License 2.0](https://github.com/GuillaumeFalourd/convert-json-to-env/blob/main/LICENSE)

<!-- ### Contribuidores

<a href="https://github.com/GuillaumeFalourd/convert-json-to-env
/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=GuillaumeFalourd/convert-json-to-env
" />
</a>

(Criado com [contributors-img](https://contrib.rocks)) -->
