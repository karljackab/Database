# csca_db
### please npm install the following packages before using
1. [mariasql](https://github.com/mscdex/node-mariasql)
2. [line-reader](https://github.com/nickewing/line-reader)
3. [generic-pool](https://github.com/coopernurse/node-pool)

## Introduction

### Personal Information of Student
| function | description |
| ------- | ----- |
| findPerson(id,cb) | return someone's profile |
| addEmail(student_id,email) | update student's e-mail |

### Course Map
| function | description |
| ------- | ----- |
| showCosMap(student_id,cb) | return the Course Map and suggest,required course relation |
| showCosMapPass(student_id,cb) | return the passing course in Course Map |

### Course Pass and Grade
| function | description |
| ------- | ----- |
| a_uploadGrade(file_path) | assistant upload grades |
| totalCredit(student_id,cb) | return someone's credits of 必選修  ((bug |
| oldGeneralCredit(student_id,cb) | return someone's credits of 舊版通識 ((bug |
| Pass(student_id,cb) | return all of someone's passing course |
