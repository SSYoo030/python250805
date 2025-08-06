import re

def is_valid_email(email):
    # 이메일 주소에 '@'가 딱 1개만 있는지 확인해요
    if email.count('@') != 1:
        return False
    # '@'를 기준으로 앞부분(local)과 뒷부분(domain)을 나눠요
    local, domain = email.split('@')
    # '@' 앞에 아무것도 없으면 안 돼요
    if not local:
        return False
    # '@' 뒤에 아무것도 없으면 안 돼요
    if not domain:
        return False
    # 도메인에 점(.)이 두 번 연속(..) 나오면 안 돼요
    if '..' in domain:
        return False
    # 도메인에 점(.)이 하나도 없으면 안 돼요
    if '.' not in domain:
        return False
    # 위 조건을 모두 통과하면 이메일이 맞아요!
    return True

# 아래는 이메일 주소가 맞는지 확인할 10개의 예시예요
test_emails = [
    "user@example.com",           # 맞는 이메일
    "test.user@domain.co.kr",     # 맞는 이메일
    "invalid-email@",             # '@' 뒤가 없어서 틀림
    "another.user@domain.com",    # 맞는 이메일
    "user123@sub.domain.com",     # 맞는 이메일
    "user.name@domain",           # 도메인에 점이 없어서 틀림
    "user@domain.c",              # 맞는 이메일(짧은 도메인도 허용)
    "user@domain.company",        # 맞는 이메일
    "user@domain..com",           # 점이 두 번 연속이라서 틀림
    "user@domain.com"             # 맞는 이메일
]

# 이메일 주소가 맞는지 하나씩 확인해서 결과를 보여줘요
for email in test_emails:
    result = "유효함" if is_valid_email(email) else "유효하지 않음"
    print(f"{email}: {result}")

# --- 5살 아이도 이해할 수 있는 설명 ---
# 이메일 주소는 꼭 '앞부분@뒷부분' 모양이어야 해요.
# 앞부분이 없거나, 뒷부분이 없으면 안 돼요.
# 뒷부분에는 점(.)이 꼭 하나 이상 있어야 해요.
# 점이 두 번 연속(..) 나오면 안 돼요.