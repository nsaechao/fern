# This file was auto-generated by Fern from our API Definition.

import uuid
import datetime

from seed import (
    TracedFile,
    ExceptionInfo,
    TraceResponse,
    TestCaseResult,
    TraceResponseV2,
    StackInformation,
    ExpressionLocation,
    ExceptionV2_Generic,
    WorkspaceRunDetails,
    TestSubmissionStatus,
    TestSubmissionUpdate,
    RunningSubmissionState,
    TestCaseResultWithStdout,
    WorkspaceSubmissionStatus,
    WorkspaceSubmissionUpdate,
    DebugVariableValue_IntegerValue,
    TestSubmissionUpdateInfo_Running,
    WorkspaceSubmissionUpdateInfo_Running,
)
from seed.client import SeedTrace, AsyncSeedTrace


async def test_update_test_submission_status(client: SeedTrace, async_client: AsyncSeedTrace) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.admin.update_test_submission_status(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), request=TestSubmissionStatus()) is None  # type: ignore[func-returns-value]
    
    assert await async_client.admin.update_test_submission_status(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), request=TestSubmissionStatus()) is None  # type: ignore[func-returns-value]
async def test_send_test_submission_update(client: SeedTrace, async_client: AsyncSeedTrace) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.admin.send_test_submission_update(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), request=TestSubmissionUpdate(update_time=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00"), update_info=TestSubmissionUpdateInfo_Running(type="running", value=RunningSubmissionState.QUEUEING_SUBMISSION))) is None  # type: ignore[func-returns-value]
    
    assert await async_client.admin.send_test_submission_update(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), request=TestSubmissionUpdate(update_time=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00"), update_info=TestSubmissionUpdateInfo_Running(type="running", value=RunningSubmissionState.QUEUEING_SUBMISSION))) is None  # type: ignore[func-returns-value]
async def test_update_workspace_submission_status(client: SeedTrace, async_client: AsyncSeedTrace) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.admin.update_workspace_submission_status(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), request=WorkspaceSubmissionStatus()) is None  # type: ignore[func-returns-value]
    
    assert await async_client.admin.update_workspace_submission_status(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), request=WorkspaceSubmissionStatus()) is None  # type: ignore[func-returns-value]
async def test_send_workspace_submission_update(client: SeedTrace, async_client: AsyncSeedTrace) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.admin.send_workspace_submission_update(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), request=WorkspaceSubmissionUpdate(update_time=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00"), update_info=WorkspaceSubmissionUpdateInfo_Running(type="running", value=RunningSubmissionState.QUEUEING_SUBMISSION))) is None  # type: ignore[func-returns-value]
    
    assert await async_client.admin.send_workspace_submission_update(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), request=WorkspaceSubmissionUpdate(update_time=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00"), update_info=WorkspaceSubmissionUpdateInfo_Running(type="running", value=RunningSubmissionState.QUEUEING_SUBMISSION))) is None  # type: ignore[func-returns-value]
async def test_store_traced_test_case(client: SeedTrace, async_client: AsyncSeedTrace) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.admin.store_traced_test_case(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), test_case_id="string", result=TestCaseResultWithStdout(result=TestCaseResult(), stdout="string"), trace_responses=[TraceResponse(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), line_number=1, return_value=DebugVariableValue_IntegerValue(type="integerValue", value=1), expression_location=ExpressionLocation(), stack=StackInformation(), stdout="string")]) is None  # type: ignore[func-returns-value]
    
    assert await async_client.admin.store_traced_test_case(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), test_case_id="string", result=TestCaseResultWithStdout(result=TestCaseResult(), stdout="string"), trace_responses=[TraceResponse(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), line_number=1, return_value=DebugVariableValue_IntegerValue(type="integerValue", value=1), expression_location=ExpressionLocation(), stack=StackInformation(), stdout="string")]) is None  # type: ignore[func-returns-value]
async def test_store_traced_test_case_v_2(client: SeedTrace, async_client: AsyncSeedTrace) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.admin.store_traced_test_case_v_2(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), test_case_id="string", request=[TraceResponseV2(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), line_number=1, file=TracedFile(), return_value=DebugVariableValue_IntegerValue(type="integerValue", value=1), expression_location=ExpressionLocation(), stack=StackInformation(), stdout="string")]) is None  # type: ignore[func-returns-value]
    
    assert await async_client.admin.store_traced_test_case_v_2(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), test_case_id="string", request=[TraceResponseV2(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), line_number=1, file=TracedFile(), return_value=DebugVariableValue_IntegerValue(type="integerValue", value=1), expression_location=ExpressionLocation(), stack=StackInformation(), stdout="string")]) is None  # type: ignore[func-returns-value]
async def test_store_traced_workspace(client: SeedTrace, async_client: AsyncSeedTrace) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.admin.store_traced_workspace(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), workspace_run_details=WorkspaceRunDetails(exception_v_2=ExceptionV2_Generic(type="generic"), exception=ExceptionInfo(), stdout="string"), trace_responses=[TraceResponse(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), line_number=1, return_value=DebugVariableValue_IntegerValue(type="integerValue", value=1), expression_location=ExpressionLocation(), stack=StackInformation(), stdout="string")]) is None  # type: ignore[func-returns-value]
    
    assert await async_client.admin.store_traced_workspace(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), workspace_run_details=WorkspaceRunDetails(exception_v_2=ExceptionV2_Generic(type="generic"), exception=ExceptionInfo(), stdout="string"), trace_responses=[TraceResponse(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), line_number=1, return_value=DebugVariableValue_IntegerValue(type="integerValue", value=1), expression_location=ExpressionLocation(), stack=StackInformation(), stdout="string")]) is None  # type: ignore[func-returns-value]
async def test_store_traced_workspace_v_2(client: SeedTrace, async_client: AsyncSeedTrace) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.admin.store_traced_workspace_v_2(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), request=[TraceResponseV2(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), line_number=1, file=TracedFile(), return_value=DebugVariableValue_IntegerValue(type="integerValue", value=1), expression_location=ExpressionLocation(), stack=StackInformation(), stdout="string")]) is None  # type: ignore[func-returns-value]
    
    assert await async_client.admin.store_traced_workspace_v_2(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), request=[TraceResponseV2(submission_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"), line_number=1, file=TracedFile(), return_value=DebugVariableValue_IntegerValue(type="integerValue", value=1), expression_location=ExpressionLocation(), stack=StackInformation(), stdout="string")]) is None  # type: ignore[func-returns-value]
