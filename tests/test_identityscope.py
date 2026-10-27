import unittest,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from identityscope import evaluate
class Tests(unittest.TestCase):
 def test_explicit_deny(self):
  p=json.loads((pathlib.Path(__file__).resolve().parents[1]/"examples/identity.json").read_text())
  self.assertEqual(evaluate(p,"s3:GetObject","arn:aws:s3:::example-bucket/private/a")["decision"],"explicitDeny")
 def test_incomplete_on_condition(self):
  p={"Statement":[{"Effect":"Allow","Action":"*","Resource":"*","Condition":{"Bool":{"x":"true"}}}]}
  self.assertFalse(evaluate(p,"s3:GetObject","*")["complete"])
