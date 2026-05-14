import json
import re


def retrieve_phone_code(driver):
    logs = driver.get_log("performance")

    for log in logs:
        message = json.loads(log["message"])["message"]

        if message["method"] != "Network.responseReceived":
            continue

        url = message.get("params", {}).get("response", {}).get("url", "")

        if "api/v1/number" not in url:
            continue

        request_id = message["params"]["requestId"]
        response_body = driver.execute_cdp_cmd(
            "Network.getResponseBody",
            {"requestId": request_id}
        )

        body = response_body.get("body", "")
        code_match = re.search(r'\d{4}', body)

        if code_match:
            return code_match.group(0)

    return None