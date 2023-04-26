"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from datetime import datetime  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)

from reconcile.gql_definitions.fragments.aws_account_common import AWSAccountCommon
from reconcile.gql_definitions.fragments.terraform_state import TerraformState


DEFINITION = """
fragment AWSAccountCommon on AWSAccount_v1 {
  path
  name
  uid
  terraformUsername
  consoleUrl
  resourcesDefaultRegion
  supportedDeploymentRegions
  providerVersion
  accountOwners {
    name
    email
  }
  automationToken {
    ... VaultSecret
  }
  garbageCollection
  enableDeletion
  deletionApprovals {
    type
    name
    expiration
  }
  disable {
    integrations
  }
  deleteKeys
  premiumSupport
  partition
}

fragment TerraformState on TerraformStateAWS_v1 {
  provider
  bucket
  region
  integrations {
    key
    integration
  }
}

fragment VaultSecret on VaultSecret_v1 {
    path
    field
    version
    format
}

query AWSAccounts($name: String) {
  accounts: awsaccounts_v1
  (
    name: $name
  )
  {
    ... AWSAccountCommon
    terraformState {
      ... TerraformState
    }
  }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union = True
        extra = Extra.forbid


class AWSAccountV1(AWSAccountCommon):
    terraform_state: Optional[TerraformState] = Field(..., alias="terraformState")


class AWSAccountsQueryData(ConfiguredBaseModel):
    accounts: Optional[list[AWSAccountV1]] = Field(..., alias="accounts")


def query(query_func: Callable, **kwargs: Any) -> AWSAccountsQueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        AWSAccountsQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return AWSAccountsQueryData(**raw_data)