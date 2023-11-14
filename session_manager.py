# session_manager.py
import json
import os
from datetime import datetime
from exceptions import SessionError

class SessionManager:
    SESSIONS_FILE = 'sessions.json'

    def __init__(self):
        self.sessions = self.load_sessions()

    def load_sessions(self):
        """Load session data from the file."""
        if not os.path.exists(self.SESSIONS_FILE):
            return []
        with open(self.SESSIONS_FILE, 'r') as file:
            return json.load(file)

    def save_session(self, session_data):
        """Save a new session, keeping only the last 3 sessions."""
        self.sessions.append(session_data)
        self.sessions = self.sessions[-3:]  # Keep only the last 3 sessions
        with open(self.SESSIONS_FILE, 'w') as file:
            json.dump(self.sessions, file, indent=4, default=str)

    def get_last_sessions(self):
        """Get data of the last three sessions."""
        return self.sessions

    def create_new_session(self, dataset, statistics):
        """Create a new session with the current dataset and statistics."""
        session_data = {
            'timestamp': datetime.now().isoformat(),
            'dataset': dataset,
            'statistics': statistics
        }
        self.save_session(session_data)
        return session_data
