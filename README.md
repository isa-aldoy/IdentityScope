# IdentityScope
Offline AWS IAM **identity-policy subset evaluator**. Calculates explicit deny, allow or implicit deny from simple JSON identity-policy statements, and flags unsupported constructs.

## Run
```sh
python identityscope.py examples/identity.json s3:GetObject arn:aws:s3:::example-bucket/private/a
python -m unittest discover -s tests -v
```
**Limitations:** Does not handle IAM conditions, NotAction, resource-based policies, permission boundaries, organization SCPs or effective AWS authorization. Any unsupported statement marks the answer incomplete. No AWS credentials required.
