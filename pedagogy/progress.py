"""Progress tracking module.

Provides simple data structures to record student progress through
SOLO taxonomy levels for specific skills. The module focuses on core
data capture functionality required for classroom use.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import List

from .planning import Skill


class SoloLevel(str, Enum):
    """Enumeration of SOLO taxonomy levels."""

    PRE_STRUCTURAL = "Pre-structural"
    UNI_STRUCTURAL = "Uni-structural"
    MULTI_STRUCTURAL = "Multi-structural"
    RELATIONAL = "Relational"
    EXTENDED_ABSTRACT = "Extended Abstract"


@dataclass
class Student:
    """Represents a student whose progress is tracked."""

    name: str
    student_id: str


@dataclass
class ProgressEntry:
    """Record of a student's SOLO level for a specific skill."""

    student: Student
    skill: Skill
    solo_level: SoloLevel
    recorded_on: date = field(default_factory=date.today)


@dataclass
class ProgressTracker:
    """Container for storing multiple progress entries."""

    entries: List[ProgressEntry] = field(default_factory=list)

    def record_progress(self, student: Student, skill: Skill, level: SoloLevel) -> None:
        """Create a new progress entry for a student and skill."""
        self.entries.append(ProgressEntry(student, skill, level))

    def get_student_progress(self, student: Student) -> List[ProgressEntry]:
        """Return all progress entries for the given student."""
        return [entry for entry in self.entries if entry.student == student]
