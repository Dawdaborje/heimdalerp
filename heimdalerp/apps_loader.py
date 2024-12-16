import requests


def load_apps():
    """
    Loads all apps with validation for API endpoints (REST and GraphQL).
    """
    from modules_management.models import (
        ModuleModel,
    )  # Assuming models are imported here

    modules = ModuleModel.objects.filter(enabled=True)

    for module in modules:
        api_url = module.api_url
        is_graphql = module.is_graphql
        graphql_query = module.graphql_query

        try:
            if is_graphql:
                # Perform GraphQL API check
                if not graphql_query:
                    module.last_api_check_status = False
                    module.last_api_check_message = "GraphQL query must be provided."
                    module.save(
                        update_fields=[
                            "last_api_check_status",
                            "last_api_check_message",
                        ]
                    )
                    continue

                response = requests.post(
                    api_url, json={"query": graphql_query}, timeout=5
                )
                if response.status_code == 200:
                    module.last_api_check_status = True
                    module.last_api_check_message = "GraphQL API is reachable."
                else:
                    module.last_api_check_status = False
                    module.last_api_check_message = f"GraphQL API responded with status code {response.status_code}."
            else:
                # Perform REST API check
                response = requests.get(api_url, timeout=5)
                if response.status_code == 200:
                    module.last_api_check_status = True
                    module.last_api_check_message = "REST API is reachable."
                else:
                    module.last_api_check_status = False
                    module.last_api_check_message = (
                        f"REST API responded with status code {response.status_code}."
                    )

            # Save the status and message fields after checks
            module.save(
                update_fields=["last_api_check_status", "last_api_check_message"]
            )

        except requests.ConnectionError:
            module.last_api_check_status = False
            module.last_api_check_message = "Unable to connect to the API."
            module.save(
                update_fields=["last_api_check_status", "last_api_check_message"]
            )

        except requests.Timeout:
            module.last_api_check_status = False
            module.last_api_check_message = "Connection to the API timed out."
            module.save(
                update_fields=["last_api_check_status", "last_api_check_message"]
            )

        except Exception as e:
            module.last_api_check_status = False
            module.last_api_check_message = f"An error occurred: {str(e)}."
            module.save(
                update_fields=["last_api_check_status", "last_api_check_message"]
            )
