from decode_verify_jwt import extract_access_token, DecodeVerifyJWT

AWS_SECRET_ACCESS_KEY='hx13ceE6laj2aQL7/gN5TZToA2rJCGdZBfEZEV1H'
AWS_ACCESS_KEY_ID='AKIAR4ZVGM5G7T2LAETC'
AWS_DEFAULT_REGION='ap-southeast-1'
AWS_COGNITO_USER_POOL_ID='ap-southeast-1_rsTKKVPCA'
AWS_COGNITO_USER_POOL_CLIENT_ID='10dbnricheb791kcfnfr7ghqtk'

cognito_jwt_token = DecodeVerifyJWT(
    user_pool_id=os.getenv("AWS_COGNITO_USER_POOL_ID"),
    user_pool_client_id=os.getenv("AWS_COGNITO_USER_POOL_CLIENT_ID"),
    region=os.getenv("AWS_DEFAULT_REGION")
)

access_token = extract_access_token()