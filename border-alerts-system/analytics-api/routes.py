from fastapi import APIRouter
from dal import *
router = APIRouter(prefix='analytics',tags=['Analytics'])


@router.get("/analytics/alerts-by-border-and-priority")
def _analytics_alerts_by_border_and_priority():
    return analytics_alerts_by_border_and_priority()

@router.get("/analytics/top-urgent-zones")
def _analytics_top_urgent_zones():
    return analytics_top_urgent_zones()

@router.get("/analytics/distance-distribution")
def _analytics_distance_distribution():
    return analytics_distance_distribution()

@router.get("/analytics/low-visibility-high-activity")
def _analytics_low_visibility_high_activity():
    return analytics_low_visibility_high_activity()

@router.get("/analytics/hot-zones")
def _analytics_hot_zones():
    return analytics_hot_zones()