"""Basic tests for planning and progress modules."""

import pathlib
import sys

# Ensure the package root is on the Python path
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

from pedagogy.planning import (
    AchievementStandard,
    ContentDescriptor,
    LessonPlan,
    Skill,
    UnitPlan,
)
from pedagogy.progress import ProgressTracker, SoloLevel, Student


def test_unit_plan_creation():
    skill = Skill("Analyse data")
    descriptor = ContentDescriptor(code="ACSSU001", description="Investigate data")
    descriptor.add_skill(skill)
    standard = AchievementStandard("Students analyse data")
    standard.add_descriptor(descriptor)

    unit = UnitPlan(title="Data Analysis", year_group=9)
    unit.add_achievement_standard(standard)
    unit.add_lesson(LessonPlan("Lesson 1"))

    assert unit.achievement_standards[0].descriptors[0].skills[0].name == "Analyse data"
    assert unit.lessons[0].title == "Lesson 1"


def test_progress_tracking():
    skill = Skill("Interpret graphs")
    student = Student(name="Alice", student_id="s1")
    tracker = ProgressTracker()
    tracker.record_progress(student, skill, SoloLevel.RELATIONAL)

    entries = tracker.get_student_progress(student)
    assert len(entries) == 1
    assert entries[0].solo_level is SoloLevel.RELATIONAL
