MESSAGE = {
    "ISNT_GITHUB_REPO": "Current directory isn't a github repository root.",
    "NO_CHANGE_DETECTED": "No file to push !",
    "CHANGE_DETECTED": "Some change on the local repository was found !",
    "ASK_COMMIT_MESSAGE": "Give a meaningful message for the commit: ",
    "INVALID_COMMIT_VARIABLE_VALUE": "The value '{}' is invalid !",
    "DEFAULT_COMMIT_SUCCEED": "Commit succeed !",
    "ASK_COMMIT_RULES": "Give a commit rules: ",
    "INVALID_COMMIT_RULE": "Invalid commit rule given ! ('{}')",
    "DEFAULT_ASK_VAR": "Give a value for the var '{}': ",
    "RULES_DESCRIPTION": "[{}] -> {}",
    "DUMP_COMMIT_RULE_NO_DESC": "<-- {} -->",
    "DUMP_COMMIT_RULE_DESC": "<-- {} -->\nDescription: {}\n"
}

# https://gitmoji.dev/
COMMIT_RULES = {
    "REMOVE": {
        "description": "Used when removing somethings from the project.",
        "message": "[🔥] - {message}",
        "ask_message": "Explain what was removed: ",
        "success": "Boom nothings here now ! 🤠"
    }, "DOC": {
        "description": "Used when adding or updating documentation.",
        "message": "[📝] - {message}",
        "ask_message": "Explain which docs did you add: ",
        "success": "Nice i like when somebody add documentation ! 🤓"
    }, "NEW": {
        "description": "Used when adding a new feature.",
        "message": "[✨] - {message}",
        "ask_message": "Explain what's new here: ",
        "success": "Wooow new feature already ? 🫨"
    }, "BUG": {
        "description": "Used when fixing a bug.",
        "message": "[🐛] - {message}",
        "ask_message": "Which bug did you fix: ",
        "success": "Why did you put bug here in the first place ? 🤨"
    }, "ADD": {
        "description": "Used when adding a minor things (Not a new feature).",
        "message": "[✅] - {message}",
        "ask_message": "Which minor update did you made: ",
        "success": "Nice somethings minor too explore ! 🤩"
    }, "COMPILER": {
        "description": "Used when fixing compiler error or warning.",
        "message": "[🚨] - Fix compiler warning or error.",
        "success": "Why did you push a code that have warning ? 😡"
    }, "REFACTOR": {
        "description": "Used when remaking a part of the code.",
        "message": "[♻️] - {message}",
        "ask_message": "What did you remake: ",
        "success": "Try making better code in the first place next time ? 😃"
    }, "TYPO": {
        "description": "Used when fixing typo.",
        "message": "[✏️] - {message}",
        "ask_message": "What typo did you remake: ",
        "success": "Actually, you misspell a word here ! 🤓"
    }, "BAD_CODE": {
        "description": "Used when writing bad code.",
        "message": "[💩] - {message}",
        "ask_message": "Explain fast: ",
        "success": "Why are you doing that ? 🤓"
    }, "REVERT": {
        "description": "Used when reverting change.",
        "message": "[⏪️] - {message}",
        "ask_message": "Why and what did you revert: ",
        "success": "BTTF ? 🤓"
    }, "DRUNK": {
        "description": "Used when writing code when drunk.",
        "message": "[🍻] - {message}",
        "ask_message": "Go sleep: ",
        "success": "This code will be remove soon."
    }, "CLEAN": {
        "description": "Used when cleaning.",
        "message": "[🗑️] - {message}",
        "ask_message": "What did you clean: ",
        "success": "Yahouh something isn't needed anymore."
    }
}