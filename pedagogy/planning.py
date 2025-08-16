"""Planning module for curriculum design.

Defines classes for skills, content descriptors, achievement standards,
lesson plans and unit plans. These classes provide simple container
structures to store curriculum information and enable linkage between
curriculum frameworks and classroom planning.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Skill:
    """Represents a specific skill within a content descriptor."""

    name: str
    description: str = ""


@dataclass
class ContentDescriptor:
    """A descriptor within an achievement standard."""

    code: str
    description: str
    skills: List[Skill] = field(default_factory=list)

    def add_skill(self, skill: Skill) -> None:
        """Attach a skill to this descriptor."""
        self.skills.append(skill)


@dataclass
class AchievementStandard:
    """Sentence from the curriculum describing expected achievement."""

    sentence: str
    descriptors: List[ContentDescriptor] = field(default_factory=list)

    def add_descriptor(self, descriptor: ContentDescriptor) -> None:
        """Attach a content descriptor to the standard."""
        self.descriptors.append(descriptor)


@dataclass
class LessonPlan:
    """A single lesson within a unit plan."""

    title: str
    activities: List[str] = field(default_factory=list)


@dataclass
class UnitPlan:
    """A unit plan mapping lessons to curriculum outcomes."""

    title: str
    year_group: int
    achievement_standards: List[AchievementStandard] = field(default_factory=list)
    lessons: List[LessonPlan] = field(default_factory=list)

    def add_achievement_standard(self, standard: AchievementStandard) -> None:
        """Add an achievement standard that the unit addresses."""
        self.achievement_standards.append(standard)

    def add_lesson(self, lesson: LessonPlan) -> None:
        """Insert a lesson into the unit plan."""
        self.lessons.append(lesson)
