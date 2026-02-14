from datetime import datetime

class AnalyticsValidationError(Exception):
    """Raised when the data fails validation checks."""
    pass

class DataQualityError(AnalyticsValidationError):
    """Raised when data values are physically impossible or logically corrupt."""
    pass

def validate_stream_data(data_row):
    try:
        if "stream_id" not in data_row:
            raise ValueError("Missing ''stream_id' in data row")

        timestamp = data_row.get("timestamp")
        if timestamp:
            event_time = datetime.fromisoformat(timestamp)
            if event_time > datetime.now():
                raise DataQualityError("Timestamp cannot be in the future")

    except (ValueError, DataQualityError) as e:
        raise AnalyticsValidationError(f"Data validation error: {e}") from e


if __name__ == "__main__":
    sample_event = {
        "stream_id": "ABC-123",
        "timestamp": "2029-01-01T12:00:00"
    }

    try:
        validate_stream_data(sample_event)
    except AnalyticsValidationError as e:
        print(e)