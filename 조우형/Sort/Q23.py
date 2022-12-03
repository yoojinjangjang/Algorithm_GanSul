'''
Sort 기출 문제 23. 국영수

학생 N명의 이름과 국어, 영어, 수학 점수가 주어집니다. 다음 조건으로 학생의 성적을 정렬하는 프로그램을 작성하세요.
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로(단, 아스키코드에서 대문자는 소문자보다 작으므로 사전 순으로 앞에 옵니다.)
'''
import sys
sys.stdin = open("input.txt", "r")


n = int(input())
grade = []
for _ in range(n):
    grade.append(input().split())

grade.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in grade:
    print(i[0])