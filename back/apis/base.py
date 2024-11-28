from fastapi import APIRouter
from apis.v1 import route_user
from apis.v1 import route_subscription
from apis.v1 import route_subscription_status
from apis.v1 import route_project
from apis.v1 import route_team
from apis.v1 import route_team_member


api_router = APIRouter()
api_router.include_router(route_user.router,prefix="/users",tags=["users"])
api_router.include_router(route_subscription.router,prefix="/subscriptions",tags=["subscriptions"])
api_router.include_router(route_subscription_status.router,prefix="/subscriptions_status",tags=["subscriptions_status"])
api_router.include_router(route_project.router,prefix="/projects",tags=["projects"])
api_router.include_router(route_team.router,prefix="/teams",tags=["teams"])
api_router.include_router(route_team_member.router,prefix="/team_members",tags=["team_members"])