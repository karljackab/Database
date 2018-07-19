exports.setResearchTitle="\
    update research_student set research_title = :new_title\
    where research_title = :research_title\
    and tname = :tname\
    and first_second = :first_second\
    and semester = :semester";

exports.setResearchLink="\
    update research_student set link = :new_link\
    where research_title = :research_title\
    and tname = :tname\
    and first_second = :first_second\
    and semester = :semester";

exports.setResearchIntro="\
    update research_student set intro = :new_intro\
    where research_title = :research_title\
    and tname = :tname\
    and first_second = :first_second\
    and semester = :semester";

exports.setResearchScore="\
    update research_student set score = :new_score\
    where research_title = :research_title\
    and tname = :tname\
    and first_second = :first_second\
    and student_id = :student_id\
    and semester = :semester";

exports.setResearchComment="\
    update research_student set comment = :new_comment\
    where research_title = :research_title\
    and tname = :tname\
    and first_second = :first_second\
    and student_id = :student_id\
    and semester = :semester"

exports.CreateNewResearch="\
    insert into research_student\
    (student_id, tname, research_title, first_second, semester)\
    values\
    (:student_id, :tname, :research_title, :first_second, :semester)";

exports.SetResearchTitle="\
    update research_student set research_title = :new_title\
    where research_title = :research_title\
    and tname = :tname\
    and first_second = :first_second\
    and semester = :semester"

exports.CreateResearchFile="\
    insert into research_file \
    values(:research_title, :tname, :file_name, :first_second, :file_path, :file_type);"

exports.CreateResearchApplyForm="\
    insert into research_apply_form\
    values(:student_id, :research_title, :tname, 0, :first_second, :semester);"

exports.SetResearchApplyFormStatus="\
    update research_apply_form set agree=:agree \
    where research_title=:research_title and tname=:tname \
    and first_second=:first_second and semester=:semester;"

exports.DeleteResearchApplyForm="\
    delete from research_apply_form \
    where research_title=:research_title and \
    tname=:tname and first_second=:first_second \
    and semester=:semester;"
