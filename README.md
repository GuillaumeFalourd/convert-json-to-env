# Convert JSON to ENV

[![Public workflows that use this action.](https://img.shields.io/endpoint?url=https%3A%2F%2Fapi-endbug.vercel.app%2Fapi%2Fgithub-actions%2Fused-by%3Faction%3DGuillaumeFalourd%2Fconvert-json-to-env%26badge%3Dtrue)](https://github.com/search?o=desc&q=GuillaumeFalourd+convert-json-to-env+path%3A.github%2Fworkflows+language%3AYAML&s=&type=Code) [![Action test on Ubuntu](https://github.com/GuillaumeFalourd/convert-json-to-env/actions/workflows/ubuntu_action_test.yml/badge.svg)](https://github.com/GuillaumeFalourd/convert-json-to-env/actions/workflows/ubuntu_action_test.yml) [![Action test on Macos](https://github.com/GuillaumeFalourd/convert-json-to-env/actions/workflows/macos_action_test.yml/badge.svg)](https://github.com/GuillaumeFalourd/convert-json-to-env/actions/workflows/macos_action_test.yml) [![Action test on Windows](https://github.com/GuillaumeFalourd/convert-json-to-env/actions/workflows/windows_action_test.yml/badge.svg)](https://github.com/GuillaumeFalourd/convert-json-to-env/actions/workflows/windows_action_test.yml)

![](https://user-images.githubusercontent.com/22433243/166232887-64d9e68d-ec7f-4a77-8253-75c614c2d0ff.png)

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
