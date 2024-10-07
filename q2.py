# 문제2
"""
전화번호가 문자열로 주어졌을 때 전화번호의 뒷자리 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수 solution을 완성하기
"""


def solution(number: str):

    number_length = len(number)

    masked_number = (
        "*" * (number_length - 4) + number[number_length - 4 : number_length]
    )

    print(masked_number)


if __name__ == "__main__":
    phone_numbers = ["01033334444", "027778888"]
    for phone_number in phone_numbers:
        solution(phone_number)
