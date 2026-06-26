# 【MCP】MCP如何设置代理进行访问worldquant论坛？Answered

- **链接**: https://support.worldquantbrain.com[L2] 【MCP】MCP如何设置代理进行访问worldquant论坛Answered_34338569572887.md
- **作者**: ZZ37826
- **发布时间/热度**: 9 months ago, 得票: 8

## 帖子正文

**遇到的问题是：**

当MCP无法通过代理访问worldquant的论坛。

在未修改前使用cursor：1.开启代理时，无法登录也无法访问论坛。2.未开启代理的时，可以登录但无法访问论坛。

修改后：开启代理时，可以登录也可以访问论坛。

plus：如果MCP无法运行，可以先开启对应的python.exe来试试pip install cnhkmcp看看会报什么错误，这也是一种排查方案。

**1.修改platform_functions.py和forum_functions.py：**

A. **platform_functions.py**

```

> #!/usr/bin/env python3
> """
> WorldQuant BRAIN MCP Server - Python Version
> A comprehensive Model Context Protocol (MCP) server for WorldQuant BRAIN platform integration.
> """
> import json
> import time
> import asyncio
> import logging
> from typing import Dict, List, Optional, Any, Union
> from dataclasses import dataclass, asdict
> from datetime import datetime, timedelta
> import os
> import sys
> from time import sleep
> import requests
> import pandas as pd
> from selenium import webdriver
> from selenium.webdriver.chrome.options import Options
> from selenium.webdriver.common.by import By
> from selenium.webdriver.support.ui import WebDriverWait
> from selenium.webdriver.support import expected_conditions as EC
> from bs4 import BeautifulSoup
> from mcp.server.fastmcp import FastMCP
> from pydantic import BaseModel, Field, EmailStr
> from pathlib import Path
> # Configure logging
> logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
> logger = logging.getLogger(__name__)
> # Pydantic models for type safety
> class AuthCredentials(BaseModel):
> email: EmailStr
> password: str
> class SimulationSettings(BaseModel):
> instrumentType: str = "EQUITY"
> region: str = "USA"
> universe: str = "TOP3000"
> delay: int = 1
> decay: float = 0.0
> neutralization: str = "NONE"
> truncation: float = 0.0
> pasteurization: str = "ON"
> unitHandling: str = "VERIFY"
> nanHandling: str = "OFF"
> language: str = "FASTEXPR"
> visualization: bool = True
> testPeriod: str = "P0Y0M"
> selectionHandling: str = "POSITIVE"
> selectionLimit: int = 1000
> maxTrade: str = "OFF"
> componentActivation: str = "IS"
> class SimulationData(BaseModel):
> type: str = "REGULAR"  # "REGULAR" or "SUPER"
> settings: SimulationSettings
> regular: Optional[str] = None
> combo: Optional[str] = None
> selection: Optional[str] = None
> class BrainApiClient:
> """WorldQuant BRAIN API client with comprehensive functionality."""
> def __init__(self):
> self.base_url = " [https://api.worldquantbrain.com](https://api.worldquantbrain.com) "
> self.session = requests.Session()
> self.auth_credentials = None
> self.is_authenticating = False
> # Configure session
> self.session.timeout = 30
> self.session.headers.update({
> 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
> })
> def log(self, message: str, level: str = "INFO"):
> """Log messages to stderr to avoid MCP protocol interference."""
> print(f"[{level}] {message}", file=sys.stderr)
> async def authenticate(self, email: str, password: str) -> Dict[str, Any]:
> """Authenticate with WorldQuant BRAIN platform with biometric support."""
> self.log("🔐 Starting Authentication process...", "INFO")
> try:
> # Store credentials for potential re-authentication
> self.auth_credentials = {'email': email, 'password': password}
> # Clear any existing session data
> self.session.cookies.clear()
> self.session.auth = None
> # Create Basic Authentication header (base64 encoded credentials)
> import base64
> credentials = f"{email}:{password}"
> encoded_credentials = base64.b64encode(credentials.encode()).decode()
> # Send POST request with Basic Authentication header
> headers = {
> 'Authorization': f'Basic {encoded_credentials}'
> }
> response = self.session.post(' [https://api.worldquantbrain.com/authentication](https://api.worldquantbrain.com/authentication) ', headers=headers)
> # Check for successful authentication (status code 201)
> if response.status_code == 201:
> self.log("Authentication successful", "SUCCESS")
> # Check if JWT token was automatically stored by session
> jwt_token = self.session.cookies.get('t')
> if jwt_token:
> self.log("JWT token automatically stored by session", "SUCCESS")
> else:
> self.log("⚠️ No JWT token found in session", "WARNING")
> # Return success response
> return {
> 'user': {'email': email},
> 'status': 'authenticated',
> 'permissions': ['read', 'write'],
> 'message': 'Authentication successful',
> 'status_code': response.status_code,
> 'has_jwt': jwt_token is not None
> }
> # Check if biometric authentication is required (401 with persona)
> elif response.status_code == 401:
> www_auth = response.headers.get("WWW-Authenticate")
> location = response.headers.get("Location")
> if www_auth == "persona" and location:
> self.log("🔴 Biometric authentication required", "INFO")
> # Handle biometric authentication
> from urllib.parse import urljoin
> biometric_url = urljoin(response.url, location)
> return await self._handle_biometric_auth(biometric_url, email)
> else:
> raise Exception("Incorrect email or password")
> else:
> raise Exception(f"Authentication failed with status code: {response.status_code}")
> except requests.HTTPError as e:
> self.log(f"❌ HTTP error during authentication: {e}", "ERROR")
> raise
> except Exception as e:
> self.log(f"❌ Authentication failed: {str(e)}", "ERROR")
> raise
> async def _handle_biometric_auth(self, biometric_url: str, email: str) -> Dict[str, Any]:
> """Handle biometric authentication using browser automation."""
> self.log("🌐 Starting biometric authentication...", "INFO")
> try:
> # Import selenium for browser automation
> from selenium import webdriver
> from selenium.webdriver.chrome.options import Options
> import time
> # Setup Chrome options
> options = Options()
> options.add_argument('--no-sandbox')
> options.add_argument('--disable-dev-shm-usage')
> driver = None
> try:
> # Open browser with timeout
> driver = webdriver.Chrome(options=options)
> # Set a short timeout so it doesn't wait forever
> driver.set_page_load_timeout(80)  # Only wait 5 seconds
> self.log("🌐 Opening browser for biometric authentication...", "INFO")
> # Try to open the URL but handle timeout
> try:
> driver.get(biometric_url)
> self.log("Browser page loaded successfully", "SUCCESS")
> except Exception as timeout_error:
> self.log(f"⚠️ Page load timeout (expected): {str(timeout_error)[:50]}...", "WARNING")
> self.log("Browser window is open for biometric authentication", "INFO")
> # Print instructions
> print("\n" + "="*60, file=sys.stderr)
> print("BIOMETRIC AUTHENTICATION REQUIRED", file=sys.stderr)
> print("="*60, file=sys.stderr)
> print("Browser window is open with biometric authentication page", file=sys.stderr)
> print("Complete the biometric authentication in the browser", file=sys.stderr)
> print("The system will automatically check when you're done...", file=sys.stderr)
> print("="*60, file=sys.stderr)
> # Keep checking until authentication is complete
> max_attempts = 60  # 5 minutes maximum (60 * 5 seconds)
> attempt = 0
> while attempt < max_attempts:
> time.sleep(5)  # Check every 5 seconds
> attempt += 1
> # Check if authentication completed
> check_response = self.session.post(biometric_url)
> self.log(f"🔄 Checking authentication status (attempt {attempt}/{max_attempts}): {check_response.status_code}", "INFO")
> if check_response.status_code == 201:
> self.log("Biometric authentication successful!", "SUCCESS")
> # Close browser
> driver.quit()
> # Check JWT token
> jwt_token = self.session.cookies.get('t')
> if jwt_token:
> self.log("JWT token received", "SUCCESS")
> # Return success response
> return {
> 'user': {'email': email},
> 'status': 'authenticated',
> 'permissions': ['read', 'write'],
> 'message': 'Biometric authentication successful',
> 'status_code': check_response.status_code,
> 'has_jwt': jwt_token is not None
> }
> # If we get here, authentication timed out
> if driver:
> driver.quit()
> raise Exception("Biometric authentication timed out")
> except Exception as driver_error:
> if driver:
> try:
> driver.quit()
> except:
> pass
> raise Exception(f"Browser automation error: {driver_error}")
> except Exception as e:
> self.log(f"❌ Biometric authentication failed: {str(e)}", "ERROR")
> raise
> async def is_authenticated(self) -> bool:
> """Check if currently authenticated using JWT token."""
> try:
> # Check if we have a JWT token in cookies
> jwt_token = self.session.cookies.get('t')
> if not jwt_token:
> self.log("❌ No JWT token found", "INFO")
> return False
> # Test authentication with a simple API call
> response = self.session.get(f"{self.base_url}/authentication")
> if response.status_code == 200:
> return True
> elif response.status_code == 401:
> self.log("❌ JWT token expired or invalid (401)", "INFO")
> return False
> else:
> self.log(f"⚠️ Unexpected status code during auth check: {response.status_code}", "WARNING")
> return False
> except Exception as e:
> self.log(f"❌ Error checking authentication: {str(e)}", "ERROR")
> return False
> async def ensure_authenticated(self):
> """Ensure authentication is valid, re-authenticate if needed."""
> if not await self.is_authenticated() and self.auth_credentials:
> self.log("🔄 Re-authenticating...", "INFO")
> await self.authenticate(self.auth_credentials['email'], self.auth_credentials['password'])
> elif not self.auth_credentials:
> raise Exception("Not authenticated and no stored credentials available. Please call authenticate() first.")
> async def get_authentication_status(self) -> Optional[Dict[str, Any]]:
> """Get current authentication status and user info."""
> try:
> response = self.session.get(f"{self.base_url}/users/self")
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get auth status: {str(e)}", "ERROR")
> return None
> async def create_simulation(self, simulation_data: SimulationData) -> Dict[str, str]:
> """Create a new simulation on BRAIN platform."""
> await self.ensure_authenticated()
> try:
> self.log("🚀 Creating simulation...", "INFO")
> # Prepare settings based on simulation type
> settings_dict = simulation_data.settings.dict()
> # Remove fields based on simulation type
> if simulation_data.type == "REGULAR":
> # Remove SUPER-specific fields for REGULAR
> settings_dict.pop('selectionHandling', None)
> settings_dict.pop('selectionLimit', None)
> settings_dict.pop('componentActivation', None)
> elif simulation_data.type == "SUPER":
> # SUPER type keeps all fields
> pass
> # Filter out None values from settings
> settings_dict = {k: v for k, v in settings_dict.items() if v is not None}
> # Prepare simulation payload
> payload = {
> 'type': simulation_data.type,
> 'settings': settings_dict
> }
> # Add type-specific fields
> if simulation_data.type == "REGULAR":
> if simulation_data.regular:
> payload['regular'] = simulation_data.regular
> elif simulation_data.type == "SUPER":
> if simulation_data.combo:
> payload['combo'] = simulation_data.combo
> if simulation_data.selection:
> payload['selection'] = simulation_data.selection
> # Filter out None values from entire payload
> payload = {k: v for k, v in payload.items() if v is not None}
> # Debug: print payload for troubleshooting
> # print("📋 Sending payload:")
> # print(json.dumps(payload, indent=2))
> response = self.session.post(f"{self.base_url}/simulations", json=payload)
> response.raise_for_status()
> # Handle empty response body - extract simulation ID from Location header
> location = response.headers.get('Location', '')
> simulation_id = location.split('/')[-1] if location else None
> self.log(f"Simulation created with ID: {simulation_id}", "SUCCESS")
> finished = False
> while True:
> simulation_progress = self.session.get(location)
> if simulation_progress.headers.get("Retry-After", 0) == 0:
> break
> print("Sleeping for " + simulation_progress.headers["Retry-After"] + " seconds")
> sleep(float(simulation_progress.headers["Retry-After"]))
> print("Alpha done simulating, getting alpha details")
> alpha_id = simulation_progress.json()["alpha"]
> alpha = self.session.get(" [https://api.worldquantbrain.com/alphas/](https://api.worldquantbrain.com/alphas/) " + alpha_id)
> return alpha.json()
> except Exception as e:
> self.log(f"❌ Failed to create simulation: {str(e)}", "ERROR")
> raise
> # get_simulation_status function removed as requested
> # wait_for_simulation function removed as requested
> async def get_alpha_details(self, alpha_id: str) -> Dict[str, Any]:
> """Get detailed information about an alpha."""
> await self.ensure_authenticated()
> try:
> response = self.session.get(f"{self.base_url}/alphas/{alpha_id}")
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get alpha details: {str(e)}", "ERROR")
> raise
> async def get_datasets(self, instrument_type: str = "EQUITY", region: str = "USA",
> delay: int = 1, universe: str = "TOP3000", theme: str = "false", search: Optional[str] = None) -> Dict[str, Any]:
> """Get available datasets."""
> await self.ensure_authenticated()
> try:
> params = {
> 'instrumentType': instrument_type,
> 'region': region,
> 'delay': delay,
> 'universe': universe,
> 'theme': theme
> }
> if search:
> params['search'] = search
> response = self.session.get(f"{self.base_url}/data-sets", params=params)
> response.raise_for_status()
> response = response.json()
> response['extraNote'] = "if your returned result is 0, you may want to check your parameter by using get_platform_setting_options tool to got correct parameter"
> return response
> except Exception as e:
> self.log(f"Failed to get datasets: {str(e)}", "ERROR")
> raise
> async def get_datafields(self, instrument_type: str = "EQUITY", region: str = "USA",
> delay: int = 1, universe: str = "TOP3000", theme: str = "false",
> dataset_id: Optional[str] = None, data_type: str = "",
> search: Optional[str] = None) -> Dict[str, Any]:
> """Get available data fields."""
> await self.ensure_authenticated()
> try:
> params = {
> 'instrumentType': instrument_type,
> 'region': region,
> 'delay': delay,
> 'universe': universe,
> 'limit': '50',
> 'offset': '0'
> }
> if data_type != 'ALL':
> params['type'] = data_type
> if dataset_id:
> params['dataset.id'] = dataset_id
> if search:
> params['search'] = search
> response = self.session.get(f"{self.base_url}/data-fields", params=params)
> response.raise_for_status()
> response = response.json()
> response['extraNote'] = "if your returned result is 0, you may want to check your parameter by using get_platform_setting_options tool to got correct parameter"
> return response
> except Exception as e:
> self.log(f"Failed to get datafields: {str(e)}", "ERROR")
> raise
> async def get_alpha_pnl(self, alpha_id: str) -> Dict[str, Any]:
> """Get PnL data for an alpha with retry logic."""
> await self.ensure_authenticated()
> max_retries = 5
> retry_delay = 2  # seconds
> for attempt in range(max_retries):
> try:
> self.log(f"Attempting to get PnL for alpha {alpha_id} (attempt {attempt + 1}/{max_retries})", "INFO")
> response = self.session.get(f"{self.base_url}/alphas/{alpha_id}/recordsets/pnl")
> response.raise_for_status()
> # Some alphas may return 204 No Content or an empty body
> text = (response.text or "").strip()
> if not text:
> if attempt < max_retries - 1:
> self.log(f"Empty PnL response for {alpha_id}, retrying in {retry_delay} seconds...", "WARNING")
> await asyncio.sleep(retry_delay)
> retry_delay *= 1.5  # Exponential backoff
> continue
> else:
> self.log(f"Empty PnL response after {max_retries} attempts for {alpha_id}", "WARNING")
> return {}
> try:
> pnl_data = response.json()
> if pnl_data:
> self.log(f"Successfully retrieved PnL data for alpha {alpha_id}", "SUCCESS")
> return pnl_data
> else:
> if attempt < max_retries - 1:
> self.log(f"Empty PnL JSON for {alpha_id}, retrying in {retry_delay} seconds...", "WARNING")
> await asyncio.sleep(retry_delay)
> retry_delay *= 1.5
> continue
> else:
> self.log(f"Empty PnL JSON after {max_retries} attempts for {alpha_id}", "WARNING")
> return {}
> except Exception as parse_err:
> if attempt < max_retries - 1:
> self.log(f"PnL JSON parse failed for {alpha_id} (attempt {attempt + 1}), retrying in {retry_delay} seconds...", "WARNING")
> await asyncio.sleep(retry_delay)
> retry_delay *= 1.5
> continue
> else:
> self.log(f"PnL JSON parse failed for {alpha_id} after {max_retries} attempts: {parse_err}", "WARNING")
> return {}
> except Exception as e:
> if attempt < max_retries - 1:
> self.log(f"Failed to get alpha PnL for {alpha_id} (attempt {attempt + 1}), retrying in {retry_delay} seconds: {str(e)}", "WARNING")
> await asyncio.sleep(retry_delay)
> retry_delay *= 1.5
> continue
> else:
> self.log(f"Failed to get alpha PnL for {alpha_id} after {max_retries} attempts: {str(e)}", "ERROR")
> raise
> # This should never be reached, but just in case
> return {}
> async def get_user_alphas(
> self,
> stage: str = "OS",
> limit: int = 30,
> offset: int = 0,
> start_date: Optional[str] = None,
> end_date: Optional[str] = None,
> submission_start_date: Optional[str] = None,
> submission_end_date: Optional[str] = None,
> order: Optional[str] = None,
> hidden: Optional[bool] = None,
> ) -> Dict[str, Any]:
> """Get user's alphas with advanced filtering."""
> await self.ensure_authenticated()
> try:
> params = {
> "stage": stage,
> "limit": limit,
> "offset": offset,
> }
> if start_date:
> params["dateCreated>"] = start_date
> if end_date:
> params["dateCreated<"] = end_date
> if submission_start_date:
> params["dateSubmitted>"] = submission_start_date
> if submission_end_date:
> params["dateSubmitted<"] = submission_end_date
> if order:
> params["order"] = order
> if hidden is not None:
> params["hidden"] = str(hidden).lower()
> response = self.session.get(f"{self.base_url}/users/self/alphas", params=params)
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get user alphas: {str(e)}", "ERROR")
> raise
> async def submit_alpha(self, alpha_id: str) -> bool:
> """Submit an alpha for production."""
> await self.ensure_authenticated()
> try:
> self.log(f"📤 Submitting alpha {alpha_id} for production...", "INFO")
> response = self.session.post(f"{self.base_url}/alphas/{alpha_id}/submit")
> response.raise_for_status()
> self.log(f"Alpha {alpha_id} submitted successfully", "SUCCESS")
> return True
> except Exception as e:
> self.log(f"❌ Failed to submit alpha: {str(e)}", "ERROR")
> return False
> async def get_events(self) -> Dict[str, Any]:
> """Get available events and competitions."""
> await self.ensure_authenticated()
> try:
> response = self.session.get(f"{self.base_url}/events")
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get events: {str(e)}", "ERROR")
> raise
> async def get_leaderboard(self, user_id: Optional[str] = None) -> Dict[str, Any]:
> """Get leaderboard data."""
> await self.ensure_authenticated()
> try:
> params = {}
> if user_id:
> params['user'] = user_id
> else:
> # Get current user ID if not specified
> user_response = self.session.get(f"{self.base_url}/users/self")
> if user_response.status_code == 200:
> user_data = user_response.json()
> params['user'] = user_data.get('id')
> response = self.session.get(f"{self.base_url}/consultant/boards/leader", params=params)
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get leaderboard: {str(e)}", "ERROR")
> raise
> async def get_operators(self) -> Dict[str, Any]:
> """Get available operators for alpha creation."""
> await self.ensure_authenticated()
> try:
> response = self.session.get(f"{self.base_url}/operators")
> response.raise_for_status()
> operators_data = response.json()
> # Ensure we return a dictionary format even if API returns a list
> if isinstance(operators_data, list):
> return {"operators": operators_data, "count": len(operators_data)}
> else:
> return operators_data
> except Exception as e:
> self.log(f"Failed to get operators: {str(e)}", "ERROR")
> raise
> async def run_selection(
> self,
> selection: str,
> instrument_type: str = "EQUITY",
> region: str = "USA",
> delay: int = 1,
> selection_limit: int = 1000,
> selection_handling: str = "POSITIVE"
> ) -> Dict[str, Any]:
> """Run a selection query to filter instruments."""
> await self.ensure_authenticated()
> try:
> selection_data = {
> "selection": selection,
> "instrumentType": instrument_type,
> "region": region,
> "delay": delay,
> "selectionLimit": selection_limit,
> "selectionHandling": selection_handling
> }
> response = self.session.get(f"{self.base_url}/simulations/super-selection", params=selection_data)
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to run selection: {str(e)}", "ERROR")
> raise
> async def get_user_profile(self, user_id: str = "self") -> Dict[str, Any]:
> """Get user profile information."""
> await self.ensure_authenticated()
> try:
> response = self.session.get(f"{self.base_url}/users/{user_id}")
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get user profile: {str(e)}", "ERROR")
> raise
> async def get_documentations(self) -> Dict[str, Any]:
> """Get available documentations and learning materials."""
> await self.ensure_authenticated()
> try:
> response = self.session.get(f"{self.base_url}/tutorials")
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get documentations: {str(e)}", "ERROR")
> raise
> # get_messages_summary function removed as requested
> async def get_messages(self, limit: Optional[int] = None, offset: int = 0) -> Dict[str, Any]:
> """Get messages for the current user with optional pagination.
> Image / large binary payload mitigation:
> Some messages embed base64 encoded images (e.g. <img src="data:image/png;base64,..."/>).
> Returning full base64 can explode token usage for an LLM client. We post-process each
> message description and (by default) extract embedded base64 images to disk and replace
> them with lightweight placeholders while preserving context.
> Strategies (environment driven in future – currently parameterless public API):
> - placeholder (default): save images to message_images/ and replace with marker text.
> - ignore: strip image tags entirely, leaving a note.
> - keep: leave description unchanged (unsafe for LLM token limits).
> A message dict gains an 'extracted_images' list when images are processed.
> """
> await self.ensure_authenticated()
> import re, base64, pathlib
> image_handling = os.environ.get("BRAIN_MESSAGE_IMAGE_MODE", "placeholder").lower()
> save_dir = pathlib.Path("message_images")
> from typing import Tuple
> def process_description(desc: str, message_id: str) -> Tuple[str, List[str]]:
> if not desc or image_handling == "keep":
> return desc, []
> attachments: List[str] = []
> # Regex to capture full <img ...> tag with data URI
> img_tag_pattern = re.compile(r"<img[^>]+src=\"(data:image/[^\"]+)\"[^>]*>", re.IGNORECASE)
> # Iterate over unique matches to avoid double work
> matches = list(img_tag_pattern.finditer(desc))
> if not matches:
> # Additional heuristic: very long base64-looking token inside quotes followed by </img>
> # (legacy format noted by user sample). Replace with placeholder.
> heuristic_pattern = re.compile(r"([A-Za-z0-9+/]{500,}={0,2})\"\s*</img>")
> if image_handling != "keep" and heuristic_pattern.search(desc):
> placeholder = "[Embedded image removed - large base64 sequence truncated]"
> return heuristic_pattern.sub(placeholder + "</img>", desc), []
> return desc, []
> # Ensure save directory exists only if we will store something
> if image_handling == "placeholder" and not save_dir.exists():
> try:
> save_dir.mkdir(parents=True, exist_ok=True)
> except Exception as e:
> self.log(f"Could not create image save directory: {e}", "WARNING")
> new_desc = desc
> for idx, match in enumerate(matches, start=1):
> data_uri = match.group(1)  # data:image/...;base64,XXXX
> if not data_uri.lower().startswith("data:image"):
> continue
> # Split header and base64 payload
> if "," not in data_uri:
> continue
> header, b64_data = data_uri.split(",", 1)
> mime_part = header.split(";")[0]  # data:image/png
> ext = "png"
> if "/" in mime_part:
> ext = mime_part.split("/")[1]
> safe_ext = (ext or "img").split("?")[0]
> placeholder_text = "[Embedded image]"
> if image_handling == "ignore":
> replacement = f"[Image removed: {safe_ext}]"
> elif image_handling == "placeholder":
> # Try decode & save
> file_name = f"{message_id}_{idx}.{safe_ext}"
> file_path = save_dir / file_name
> try:
> # Guard extremely large strings (>5MB ~ 6.7M base64 chars) to avoid memory blow
> if len(b64_data) > 7_000_000:
> raise ValueError("Image too large to decode safely")
> with open(file_path, "wb") as f:
> f.write(base64.b64decode(b64_data))
> attachments.append(str(file_path))
> replacement = f"[Image extracted -> {file_path}]"
> except Exception as e:
> self.log(f"Failed to decode embedded image in message {message_id}: {e}", "WARNING")
> replacement = "[Image extraction failed - content omitted]"
> else:  # keep
> replacement = placeholder_text  # shouldn't be used since early return, but safe
> # Replace only the matched tag (not global) – use re.sub with count=1 on substring slice
> # Safer to operate on new_desc using the exact matched string
> original_tag = match.group(0)
> new_desc = new_desc.replace(original_tag, replacement, 1)
> return new_desc, attachments
> try:
> params = {}
> if limit is not None:
> params['limit'] = limit
> if offset > 0:
> params['offset'] = offset
> response = self.session.get(f"{self.base_url}/users/self/messages", params=params)
> response.raise_for_status()
> data = response.json()
> # Post-process results for image handling
> results = data.get('results', [])
> for msg in results:
> try:
> desc = msg.get('description')
> processed_desc, attachments = process_description(desc, msg.get('id', 'msg'))
> if attachments or desc != processed_desc:
> msg['description'] = processed_desc
> if attachments:
> msg['extracted_images'] = attachments
> else:
> # If changed but no attachments (ignore mode) mark sanitized
> msg['sanitized'] = True
> except Exception as inner_e:
> self.log(f"Failed to sanitize message {msg.get('id')}: {inner_e}", "WARNING")
> data['results'] = results
> data['image_handling'] = image_handling
> return data
> except Exception as e:
> self.log(f"Failed to get messages: {str(e)}", "ERROR")
> raise
> async def get_glossary_terms(self, email: str, password: str, headless: bool = False) -> Dict[str, Any]:
> """Get glossary terms from forum."""
> try:
> # Import and use forum functions
> from forum_functions import forum_client
> return await forum_client.get_glossary_terms(email, password, headless)
> except ImportError:
> self.log("Forum functions not available - install selenium and run forum_functions.py", "WARNING")
> return {"error": "Forum functions require selenium. Use forum_functions.py directly."}
> except Exception as e:
> self.log(f"Glossary extraction failed: {str(e)}", "ERROR")
> return {"error": str(e)}
> async def search_forum_posts(self, email: str, password: str, search_query: str,
> max_results: int = 50, headless: bool = True) -> Dict[str, Any]:
> """Search forum posts."""
> try:
> # Import and use forum functions
> from forum_functions import forum_client
> return await forum_client.search_forum_posts(email, password, search_query, max_results, headless)
> except ImportError:
> self.log("Forum functions not available - install selenium and run forum_functions.py", "WARNING")
> return {"error": "Forum functions require selenium. Use forum_functions.py directly."}
> except Exception as e:
> self.log(f"Forum search failed: {str(e)}", "ERROR")
> return {"error": str(e)}
> async def read_forum_post(self, email: str, password: str, article_id: str,
> headless: bool = False) -> Dict[str, Any]:
> """Get forum post."""
> try:
> # Import and use forum functions
> from forum_functions import forum_client
> return await forum_client.read_full_forum_post(email, password, article_id, headless, include_comments=True)
> except ImportError:
> self.log("Forum functions not available - install selenium and run forum_functions.py", "WARNING")
> return {"error": "Forum functions require selenium. Use forum_functions.py directly."}
> except Exception as e:
> self.log(f"Forum post retrieval failed: {str(e)}", "ERROR")
> return {"error": str(e)}
> async def get_alpha_yearly_stats(self, alpha_id: str) -> Dict[str, Any]:
> """Get yearly statistics for an alpha with retry logic."""
> await self.ensure_authenticated()
> max_retries = 5
> retry_delay = 2  # seconds
> for attempt in range(max_retries):
> try:
> self.log(f"Attempting to get yearly stats for alpha {alpha_id} (attempt {attempt + 1}/{max_retries})", "INFO")
> response = self.session.get(f"{self.base_url}/alphas/{alpha_id}/recordsets/yearly-stats")
> response.raise_for_status()
> # Check if response has content
> text = (response.text or "").strip()
> if not text:
> if attempt < max_retries - 1:
> self.log(f"Empty yearly stats response for {alpha_id}, retrying in {retry_delay} seconds...", "WARNING")
> await asyncio.sleep(retry_delay)
> retry_delay *= 1.5  # Exponential backoff
> continue
> else:
> self.log(f"Empty yearly stats response after {max_retries} attempts for {alpha_id}", "WARNING")
> return {}
> try:
> yearly_stats = response.json()
> if yearly_stats:
> self.log(f"Successfully retrieved yearly stats for alpha {alpha_id}", "SUCCESS")
> return yearly_stats
> else:
> if attempt < max_retries - 1:
> self.log(f"Empty yearly stats JSON for {alpha_id}, retrying in {retry_delay} seconds...", "WARNING")
> await asyncio.sleep(retry_delay)
> retry_delay *= 1.5
> continue
> else:
> self.log(f"Empty yearly stats JSON after {max_retries} attempts for {alpha_id}", "WARNING")
> return {}
> except Exception as parse_err:
> if attempt < max_retries - 1:
> self.log(f"Yearly stats JSON parse failed for {alpha_id} (attempt {attempt + 1}), retrying in {retry_delay} seconds...", "WARNING")
> await asyncio.sleep(retry_delay)
> retry_delay *= 1.5
> continue
> else:
> self.log(f"Yearly stats JSON parse failed for {alpha_id} after {max_retries} attempts: {parse_err}", "WARNING")
> return {}
> except Exception as e:
> if attempt < max_retries - 1:
> self.log(f"Failed to get alpha yearly stats for {alpha_id} (attempt {attempt + 1}), retrying in {retry_delay} seconds: {str(e)}", "WARNING")
> await asyncio.sleep(retry_delay)
> retry_delay *= 1.5
> continue
> else:
> self.log(f"Failed to get alpha yearly stats for {alpha_id} after {max_retries} attempts: {str(e)}", "ERROR")
> raise
> # This should never be reached, but just in case
> return {}
> async def get_production_correlation(self, alpha_id: str) -> Dict[str, Any]:
> """Get production correlation data for an alpha with retry logic."""
> await self.ensure_authenticated()
> max_retries = 5
> retry_delay = 20  # seconds
> for attempt in range(max_retries):
> try:
> self.log(f"Attempting to get production correlation for alpha {alpha_id} (attempt {attempt + 1}/{max_retries})", "INFO")
> response = self.session.get(f"{self.base_url}/alphas/{alpha_id}/correlations/prod")
> response.raise_for_status()
> # Check if response has content
> text = (response.text or "").strip()
> if not text:
> if attempt < max_retries - 1:
> self.log(f"Empty production correlation response for {alpha_id}, retrying in {retry_delay} seconds...", "WARNING")
> await asyncio.sleep(retry_delay)
> continue
> else:
> self.log(f"Empty production correlation response after {max_retries} attempts for {alpha_id}", "WARNING")
> return {}
> try:
> correlation_data = response.json()
> if correlation_data:
> self.log(f"Successfully retrieved production correlation for alpha {alpha_id}", "SUCCESS")
> return correlation_data
> else:
> if attempt < max_retries - 1:
> self.log(f"Empty production correlation JSON for {alpha_id}, retrying in {retry_delay} seconds...", "WARNING")
> await asyncio.sleep(retry_delay)
> continue
> else:
> self.log(f"Empty production correlation JSON after {max_retries} attempts for {alpha_id}", "WARNING")
> return {}
> except Exception as parse_err:
> if attempt < max_retries - 1:
> self.log(f"Production correlation JSON parse failed for {alpha_id} (attempt {attempt + 1}), retrying in {retry_delay} seconds...", "WARNING")
> await asyncio.sleep(retry_delay)
> continue
> else:
> self.log(f"Production correlation JSON parse failed for {alpha_id} after {max_retries} attempts: {parse_err}", "WARNING")
> return {}
> except Exception as e:
> if attempt < max_retries - 1:
> self.log(f"Failed to get production correlation for {alpha_id} (attempt {attempt + 1}), retrying in {retry_delay} seconds: {str(e)}", "WARNING")
> await asyncio.sleep(retry_delay)
> continue
> else:
> self.log(f"Failed to get production correlation for {alpha_id} after {max_retries} attempts: {str(e)}", "ERROR")
> raise
> # This should never be reached, but just in case
> return {}
> async def get_self_correlation(self, alpha_id: str) -> Dict[str, Any]:
> """Get self-correlation data for an alpha with retry logic."""
> await self.ensure_authenticated()
> max_retries = 5
> retry_delay = 20  # seconds
> for attempt in range(max_retries):
> try:
> self.log(f"Attempting to get self correlation for alpha {alpha_id} (attempt {attempt + 1}/{max_retries})", "INFO")
> response = self.session.get(f"{self.base_url}/alphas/{alpha_id}/correlations/self")
> response.raise_for_status()
> # Check if response has content
> text = (response.text or "").strip()
> if not text:
> if attempt < max_retries - 1:
> self.log(f"Empty self correlation response for {alpha_id}, retrying in {retry_delay} seconds...", "WARNING")
> await asyncio.sleep(retry_delay)
> continue
> else:
> self.log(f"Empty self correlation response after {max_retries} attempts for {alpha_id}", "WARNING")
> return {}
> try:
> correlation_data = response.json()
> if correlation_data:
> self.log(f"Successfully retrieved self correlation for alpha {alpha_id}", "SUCCESS")
> return correlation_data
> else:
> if attempt < max_retries - 1:
> self.log(f"Empty self correlation JSON for {alpha_id}, retrying in {retry_delay} seconds...", "WARNING")
> await asyncio.sleep(retry_delay)
> continue
> else:
> self.log(f"Empty self correlation JSON after {max_retries} attempts for {alpha_id}", "WARNING")
> return {}
> except Exception as parse_err:
> if attempt < max_retries - 1:
> self.log(f"Self correlation JSON parse failed for {alpha_id} (attempt {attempt + 1}), retrying in {retry_delay} seconds...", "WARNING")
> await asyncio.sleep(retry_delay)
> continue
> else:
> self.log(f"Self correlation JSON parse failed for {alpha_id} after {max_retries} attempts: {parse_err}", "WARNING")
> return {}
> except Exception as e:
> if attempt < max_retries - 1:
> self.log(f"Failed to get self correlation for {alpha_id} (attempt {attempt + 1}), retrying in {retry_delay} seconds: {str(e)}", "WARNING")
> await asyncio.sleep(retry_delay)
> continue
> else:
> self.log(f"Failed to get self correlation for {alpha_id} after {max_retries} attempts: {str(e)}", "ERROR")
> raise
> # This should never be reached, but just in case
> return {}
> async def check_correlation(self, alpha_id: str, correlation_type: str = "both", threshold: float = 0.7) -> Dict[str, Any]:
> """Check alpha correlation against production alphas, self alphas, or both."""
> await self.ensure_authenticated()
> try:
> results = {
> 'alpha_id': alpha_id,
> 'threshold': threshold,
> 'correlation_type': correlation_type,
> 'checks': {}
> }
> # Determine which correlations to check
> check_types = []
> if correlation_type == "both":
> check_types = ["production", "self"]
> else:
> check_types = [correlation_type]
> all_passed = True
> for check_type in check_types:
> if check_type == "production":
> correlation_data = await self.get_production_correlation(alpha_id)
> elif check_type == "self":
> correlation_data = await self.get_self_correlation(alpha_id)
> else:
> continue
> # Analyze correlation data
> if correlation_data and 'results' in correlation_data:
> correlations = correlation_data['results']
> max_correlation = max([corr.get('correlation', 0) for corr in correlations]) if correlations else 0
> passes_check = max_correlation < threshold
> else:
> max_correlation = 0
> passes_check = True
> results['checks'][check_type] = {
> 'max_correlation': max_correlation,
> 'passes_check': passes_check,
> 'correlation_data': correlation_data
> }
> if not passes_check:
> all_passed = False
> results['all_passed'] = all_passed
> return results
> except Exception as e:
> self.log(f"Failed to check correlation: {str(e)}", "ERROR")
> raise
> async def get_submission_check(self, alpha_id: str) -> Dict[str, Any]:
> """Comprehensive pre-submission check."""
> await self.ensure_authenticated()
> try:
> # Get correlation checks using the unified function
> correlation_checks = await self.check_correlation(alpha_id, correlation_type="both")
> # Get alpha details for additional validation
> alpha_details = await self.get_alpha_details(alpha_id)
> # Compile comprehensive check results
> checks = {
> 'correlation_checks': correlation_checks,
> 'alpha_details': alpha_details,
> 'all_passed': correlation_checks['all_passed']
> }
> return checks
> except Exception as e:
> self.log(f"Failed to get submission check: {str(e)}", "ERROR")
> raise
> async def set_alpha_properties(self, alpha_id: str, name: Optional[str] = None,
> color: Optional[str] = None, tags: List[str] = None,
> selection_desc: str = "None", combo_desc: str = "None") -> Dict[str, Any]:
> """Update alpha properties (name, color, tags, descriptions)."""
> await self.ensure_authenticated()
> try:
> data = {}
> if name:
> data['name'] = name
> if color:
> data['color'] = color
> if tags:
> data['tags'] = tags
> if selection_desc:
> data['selectionDesc'] = selection_desc
> if combo_desc:
> data['comboDesc'] = combo_desc
> response = self.session.patch(f"{self.base_url}/alphas/{alpha_id}", json=data)
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to set alpha properties: {str(e)}", "ERROR")
> raise
> async def get_record_sets(self, alpha_id: str) -> Dict[str, Any]:
> """List available record sets for an alpha."""
> await self.ensure_authenticated()
> try:
> response = self.session.get(f"{self.base_url}/alphas/{alpha_id}/recordsets")
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get record sets: {str(e)}", "ERROR")
> raise
> async def get_record_set_data(self, alpha_id: str, record_set_name: str) -> Dict[str, Any]:
> """Get data from a specific record set."""
> await self.ensure_authenticated()
> try:
> response = self.session.get(f"{self.base_url}/alphas/{alpha_id}/recordsets/{record_set_name}")
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get record set data: {str(e)}", "ERROR")
> raise
> async def get_user_activities(self, user_id: str, grouping: Optional[str] = None) -> Dict[str, Any]:
> """Get user activity diversity data."""
> await self.ensure_authenticated()
> try:
> params = {}
> if grouping:
> params['grouping'] = grouping
> response = self.session.get(f"{self.base_url}/users/{user_id}/activities", params=params)
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get user activities: {str(e)}", "ERROR")
> raise
> async def get_pyramid_multipliers(self) -> Dict[str, Any]:
> """Get current pyramid multipliers showing BRAIN's encouragement levels."""
> await self.ensure_authenticated()
> try:
> # Use the correct endpoint without parameters
> response = self.session.get(f"{self.base_url}/users/self/activities/pyramid-multipliers")
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get pyramid multipliers: {str(e)}", "ERROR")
> raise
> async def get_pyramid_alphas(self, start_date: Optional[str] = None,
> end_date: Optional[str] = None) -> Dict[str, Any]:
> """Get user's current alpha distribution across pyramid categories."""
> await self.ensure_authenticated()
> try:
> params = {}
> if start_date:
> params['startDate'] = start_date
> if end_date:
> params['endDate'] = end_date
> # Try the user-specific activities endpoint first (like pyramid-multipliers)
> response = self.session.get(f"{self.base_url}/users/self/activities/pyramid-alphas", params=params)
> # If that fails, try alternative endpoints
> if response.status_code == 404:
> # Try alternative endpoint structure
> response = self.session.get(f"{self.base_url}/users/self/pyramid/alphas", params=params)
> if response.status_code == 404:
> # Try yet another alternative
> response = self.session.get(f"{self.base_url}/activities/pyramid-alphas", params=params)
> if response.status_code == 404:
> # Return an informative error with what we tried
> return {
> "error": "Pyramid alphas endpoint not found",
> "tried_endpoints": [
> "/users/self/activities/pyramid-alphas",
> "/users/self/pyramid/alphas",
> "/activities/pyramid-alphas",
> "/pyramid/alphas"
> ],
> "suggestion": "This endpoint may not be available in the current API version"
> }
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get pyramid alphas: {str(e)}", "ERROR")
> raise
> async def get_user_competitions(self, user_id: Optional[str] = None) -> Dict[str, Any]:
> """Get list of competitions that the user is participating in."""
> await self.ensure_authenticated()
> try:
> if not user_id:
> # Get current user ID if not specified
> user_response = self.session.get(f"{self.base_url}/users/self")
> if user_response.status_code == 200:
> user_data = user_response.json()
> user_id = user_data.get('id')
> else:
> user_id = 'self'
> response = self.session.get(f"{self.base_url}/users/{user_id}/competitions")
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get user competitions: {str(e)}", "ERROR")
> raise
> async def get_competition_details(self, competition_id: str) -> Dict[str, Any]:
> """Get detailed information about a specific competition."""
> await self.ensure_authenticated()
> try:
> response = self.session.get(f"{self.base_url}/competitions/{competition_id}")
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get competition details: {str(e)}", "ERROR")
> raise
> async def get_competition_agreement(self, competition_id: str) -> Dict[str, Any]:
> """Get the rules, terms, and agreement for a specific competition."""
> await self.ensure_authenticated()
> try:
> response = self.session.get(f"{self.base_url}/competitions/{competition_id}/agreement")
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get competition agreement: {str(e)}", "ERROR")
> raise
> async def get_platform_setting_options(self) -> Dict[str, Any]:
> """Get available instrument types, regions, delays, and universes."""
> await self.ensure_authenticated()
> try:
> # Use OPTIONS method on simulations endpoint to get configuration options
> response = self.session.options(f"{self.base_url}/simulations")
> response.raise_for_status()
> # Parse the settings structure from the response
> settings_data = response.json()
> settings_options = settings_data['actions']['POST']['settings']['children']
> # Extract instrument configuration options
> instrument_type_data = {}
> region_data = {}
> universe_data = {}
> delay_data = {}
> neutralization_data = {}
> # Parse each setting type
> for key, setting in settings_options.items():
> if setting['type'] == 'choice':
> if setting['label'] == 'Instrument type':
> instrument_type_data = setting['choices']
> elif setting['label'] == 'Region':
> region_data = setting['choices']['instrumentType']
> elif setting['label'] == 'Universe':
> universe_data = setting['choices']['instrumentType']
> elif setting['label'] == 'Delay':
> delay_data = setting['choices']['instrumentType']
> elif setting['label'] == 'Neutralization':
> neutralization_data = setting['choices']['instrumentType']
> # Build comprehensive instrument options
> data_list = []
> for instrument_type in instrument_type_data:
> for region in region_data[instrument_type['value']]:
> for delay in delay_data[instrument_type['value']]['region'][region['value']]:
> row = {
> 'InstrumentType': instrument_type['value'],
> 'Region': region['value'],
> 'Delay': delay['value']
> }
> row['Universe'] = [
> item['value'] for item in universe_data[instrument_type['value']]['region'][region['value']]
> ]
> row['Neutralization'] = [
> item['value'] for item in neutralization_data[instrument_type['value']]['region'][region['value']]
> ]
> data_list.append(row)
> # Return structured data
> return {
> 'instrument_options': data_list,
> 'total_combinations': len(data_list),
> 'instrument_types': [item['value'] for item in instrument_type_data],
> 'regions_by_type': {
> item['value']: [r['value'] for r in region_data[item['value']]]
> for item in instrument_type_data
> }
> }
> except Exception as e:
> self.log(f"Failed to get instrument options: {str(e)}", "ERROR")
> raise
> async def performance_comparison(self, alpha_id: str, team_id: Optional[str] = None,
> competition: Optional[str] = None) -> Dict[str, Any]:
> """Get performance comparison data for an alpha."""
> await self.ensure_authenticated()
> try:
> params = {}
> if team_id:
> params['team_id'] = team_id
> if competition:
> params['competition'] = competition
> response = self.session.get(f"{self.base_url}/alphas/{alpha_id}/performance-comparison", params=params)
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get performance comparison: {str(e)}", "ERROR")
> raise
> # combine_test_results function removed as requested
> async def expand_nested_data(self, data: List[Dict[str, Any]], preserve_original: bool = True) -> List[Dict[str, Any]]:
> """Flatten complex nested data structures into tabular format."""
> try:
> expanded_data = []
> for item in data:
> expanded_item = {}
> for key, value in item.items():
> if isinstance(value, dict):
> # Expand nested dictionary
> for nested_key, nested_value in value.items():
> expanded_key = f"{key}_{nested_key}"
> expanded_item[expanded_key] = nested_value
> # Preserve original if requested
> if preserve_original:
> expanded_item[key] = value
> elif isinstance(value, list):
> # Handle list values
> expanded_item[key] = str(value) if value else []
> # Preserve original if requested
> if preserve_original:
> expanded_item[key] = value
> else:
> # Simple value
> expanded_item[key] = value
> expanded_data.append(expanded_item)
> return expanded_data
> except Exception as e:
> self.log(f"Failed to expand nested data: {str(e)}", "ERROR")
> raise
> # generate_alpha_links function removed as requested
> async def read_specific_documentation(self, page_id: str) -> Dict[str, Any]:
> """Retrieve detailed content of a specific documentation page/article."""
> await self.ensure_authenticated()
> try:
> response = self.session.get(f"{self.base_url}/tutorial-pages/{page_id}")
> response.raise_for_status()
> return response.json()
> except Exception as e:
> self.log(f"Failed to get documentation page: {str(e)}", "ERROR")
> raise
> # Badge status function removed as requested
> # Initialize MCP server
> mcp = FastMCP('brain_mcp_server')
> # Initialize API client
> brain_client = BrainApiClient()
> # Configuration management
> CONFIG_FILE = "user_config.json"
> def _resolve_config_path(for_write: bool = False) -> str:
> """
> Resolve the config file path with this priority:
> 1) BRAIN_CONFIG_PATH (file or directory)
> 2) Directory of running script when available, else current working directory
> 3) Current working directory
> When for_write=True, returns the preferred path even if it doesn't exist yet.
> """
> # 1) Explicit override via env var
> env_path = os.environ.get("BRAIN_CONFIG_PATH")
> if env_path:
> p = Path(env_path).expanduser()
> target = p / CONFIG_FILE if p.is_dir() else p
> # For read, only if it exists; for write, allow regardless
> if for_write or target.exists():
> return str(target.resolve())
> # 2) Script/module directory when available, else CWD (works in notebooks)
> base_dir = Path.cwd()
> try:
> # __file__ is not defined in notebooks; this will fail there and keep CWD
> script_dir = Path(__file__).resolve().parent  # type: ignore[name-defined]
> base_dir = script_dir
> except Exception:
> # Fall back to current working directory for notebooks/REPL
> pass
> module_path = base_dir / CONFIG_FILE
> if not for_write and module_path.exists():
> return str(module_path.resolve())
> # 3) Fallback to CWD for backward compatibility
> cwd_path = Path.cwd() / CONFIG_FILE
> if not for_write and cwd_path.exists():
> return str(cwd_path.resolve())
> # For writes (or when nothing exists), prefer the module/base directory
> return str(module_path.resolve())
> def load_config() -> Dict[str, Any]:
> """Load configuration from file with robust path resolution.
> Looks for the config in this order: BRAIN_CONFIG_PATH -> module directory -> CWD.
> Returns an empty dict when not found or on error.
> """
> path = _resolve_config_path(for_write=False)
> if os.path.exists(path):
> try:
> with open(path, 'r', encoding='utf-8') as f:
> return json.load(f)
> except Exception as e:
> logger.error(f"Failed to load config from '{path}': {e}")
> return {}
> def save_config(config: Dict[str, Any]):
> """Save configuration to file using the resolved config path.
> Uses BRAIN_CONFIG_PATH if set; otherwise writes next to this module.
> Ensures the target directory exists.
> """
> try:
> path = _resolve_config_path(for_write=True)
> os.makedirs(os.path.dirname(path), exist_ok=True)
> with open(path, 'w', encoding='utf-8') as f:
> json.dump(config, f, indent=2, ensure_ascii=False)
> except Exception as e:
> logger.error(f"Failed to save config: {e}")
> # MCP Tools
> @mcp.tool()
> async def authenticate(email: Optional[str] = "", password: Optional[str] = "") -> Dict[str, Any]:
> """
> 🔐 Authenticate with WorldQuant BRAIN platform.
> This is the first step in any BRAIN workflow. You must authenticate before using any other tools.
> Args:
> email: Your BRAIN platform email address (optional if in config or .brain_credentials)
> password: Your BRAIN platform password (optional if in config or .brain_credentials)
> Returns:
> Authentication result with user info and permissions
> """
> try:
> config = load_config()
> if 'credentials' in config:
> if not email:
> email = config['credentials'].get('email', '')
> if not password:
> password = config['credentials'].get('password', '')
> if not email or not password:
> return {"error": "Email and password required. Either provide them as arguments, configure them in user_config.json, or create a .brain_credentials file in your home directory with format: [\"email\", \"password\"]"}
> result = await brain_client.authenticate(email, password)
> # Save credentials to config for future use
> config = load_config()
> if 'credentials' not in config:
> config['credentials'] = {}
> config['credentials']['email'] = email
> config['credentials']['password'] = password
> save_config(config)
> return result
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def manage_config(action: str = "get", settings: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
> """
> 🔧 Manage configuration settings - get or update configuration.
> Args:
> action: Action to perform ("get" to retrieve config, "set" to update config)
> settings: Configuration settings to update (required when action="set")
> Returns:
> Current or updated configuration including authentication status
> """
> if action == "get":
> config = load_config()
> auth_status = await brain_client.get_authentication_status()
> return {
> "config": config,
> "auth_status": auth_status,
> "is_authenticated": await brain_client.is_authenticated()
> }
> elif action == "set":
> if settings is None:
> return {"error": "Settings parameter is required when action='set'"}
> config = load_config()
> config.update(settings)
> save_config(config)
> return config
> else:
> return {"error": f"Invalid action '{action}'. Use 'get' or 'set'."}
> @mcp.tool()
> async def create_simulation(
> type: str = "REGULAR",
> instrument_type: str = "EQUITY",
> region: str = "USA",
> universe: str = "TOP3000",
> delay: int = 1,
> decay: float = 0.0,
> neutralization: str = "NONE",
> truncation: float = 0.0,
> test_period: str = "P0Y0M",
> unit_handling: str = "VERIFY",
> nan_handling: str = "OFF",
> language: str = "FASTEXPR",
> visualization: bool = True,
> regular: Optional[str] = None,
> combo: Optional[str] = None,
> selection: Optional[str] = None,
> pasteurization: str = "ON",
> max_trade: str = "OFF",
> selection_handling: str = "POSITIVE",
> selection_limit: int = 1000,
> component_activation: str = "IS"
> ) -> Dict[str, Any]:
> """
> 🚀 Create a new simulation on BRAIN platform.
> This tool creates and starts a simulation with your alpha code. Use this after you have your alpha formula ready.
> Args:
> type: Simulation type ("REGULAR" or "SUPER")
> instrument_type: Type of instruments (e.g., "EQUITY")
> region: Market region (e.g., "USA")
> universe: Universe of stocks (e.g., "TOP3000")
> delay: Data delay (0 or 1)
> decay: Decay value for the simulation
> neutralization: Neutralization method
> truncation: Truncation value
> test_period: Test period (e.g., "P0Y0M" for 1 year 6 months)
> unit_handling: Unit handling method
> nan_handling: NaN handling method
> language: Expression language (e.g., "FASTEXPR")
> visualization: Enable visualization
> regular: Regular simulation code (for REGULAR type)
> combo: Combo code (for SUPER type)
> selection: Selection code (for SUPER type)
> Returns:
> Simulation creation result with ID and location
> """
> try:
> settings = SimulationSettings(
> instrumentType=instrument_type,
> region=region,
> universe=universe,
> delay=delay,
> decay=decay,
> neutralization=neutralization,
> truncation=truncation,
> testPeriod=test_period,
> unitHandling=unit_handling,
> nanHandling=nan_handling,
> language=language,
> visualization=visualization
> )
> simulation_data = SimulationData(
> type=type,
> settings=settings,
> regular=regular,
> combo=combo,
> selection=selection
> )
> result = await brain_client.create_simulation(simulation_data)
> return result
> except Exception as e:
> return {"error": str(e)}
> # get_simulation_status MCP tool removed as requested
> # wait_for_simulation MCP tool removed as requested
> @mcp.tool()
> async def get_alpha_details(alpha_id: str) -> Dict[str, Any]:
> """
> 📋 Get detailed information about an alpha.
> Args:
> alpha_id: The ID of the alpha to retrieve
> Returns:
> Detailed alpha information
> """
> try:
> return await brain_client.get_alpha_details(alpha_id)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_datasets(
> instrument_type: str = "EQUITY",
> region: str = "USA",
> delay: int = 1,
> universe: str = "TOP3000",
> theme: str = "false",
> search: Optional[str] = None
> ) -> Dict[str, Any]:
> """
> 📚 Get available datasets for research.
> Use this to discover what data is available for your alpha research.
> Args:
> instrument_type: Type of instruments (e.g., "EQUITY")
> region: Market region (e.g., "USA")
> delay: Data delay (0 or 1)
> universe: Universe of stocks (e.g., "TOP3000")
> theme: Theme filter
> Returns:
> Available datasets
> """
> try:
> return await brain_client.get_datasets(instrument_type, region, delay, universe, theme,search)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_datafields(
> instrument_type: str = "EQUITY",
> region: str = "USA",
> delay: int = 1,
> universe: str = "TOP3000",
> theme: str = "false",
> dataset_id: Optional[str] = None,
> data_type: str = "",
> search: Optional[str] = None
> ) -> Dict[str, Any]:
> """
> 🔍 Get available data fields for alpha construction.
> Use this to find specific data fields you can use in your alpha formulas.
> Args:
> instrument_type: Type of instruments (e.g., "EQUITY")
> region: Market region (e.g., "USA")
> delay: Data delay (0 or 1)
> universe: Universe of stocks (e.g., "TOP3000")
> theme: Theme filter
> dataset_id: Specific dataset ID to filter by
> data_type: Type of data (e.g., "MATRIX")
> search: Search term to filter fields
> Returns:
> Available data fields
> """
> try:
> return await brain_client.get_datafields(
> instrument_type, region, delay, universe, theme,
> dataset_id, data_type, search
> )
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_alpha_pnl(alpha_id: str) -> Dict[str, Any]:
> """
> 📈 Get PnL (Profit and Loss) data for an alpha.
> Args:
> alpha_id: The ID of the alpha
> Returns:
> PnL data for the alpha
> """
> try:
> return await brain_client.get_alpha_pnl(alpha_id)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_user_alphas(
> stage: str = "IS",
> limit: int = 30,
> offset: int = 0,
> start_date: Optional[str] = None,
> end_date: Optional[str] = None,
> submission_start_date: Optional[str] = None,
> submission_end_date: Optional[str] = None,
> order: Optional[str] = None,
> hidden: Optional[bool] = None,
> ) -> Dict[str, Any]:
> """
> 👤 Get user's alphas with advanced filtering, pagination, and sorting.
> This tool retrieves a list of your alphas, allowing for detailed filtering based on stage,
> creation date, submission date, and visibility. It also supports pagination and custom sorting.
> Args:
> stage (str): The stage of the alphas to retrieve.
> - "IS": In-Sample (alphas that have not been submitted).
> - "OS": Out-of-Sample (alphas that have been submitted).
> Defaults to "IS".
> limit (int): The maximum number of alphas to return in a single request.
> For example, `limit=50` will return at most 50 alphas. Defaults to 30.
> offset (int): The number of alphas to skip from the beginning of the list.
> Used for pagination. For example, `limit=50, offset=50` will retrieve alphas 51-100.
> Defaults to 0.
> start_date (Optional[str]): The earliest creation date for the alphas to be included.
> Filters for alphas created on or after this date.
> Example format: "2023-01-01T00:00:00Z".
> end_date (Optional[str]): The latest creation date for the alphas to be included.
> Filters for alphas created before this date.
> Example format: "2023-12-31T23:59:59Z".
> submission_start_date (Optional[str]): The earliest submission date for the alphas.
> Only applies to "OS" alphas. Filters for alphas submitted on or after this date.
> Example format: "2024-01-01T00:00:00Z".
> submission_end_date (Optional[str]): The latest submission date for the alphas.
> Only applies to "OS" alphas. Filters for alphas submitted before this date.
> Example format: "2024-06-30T23:59:59Z".
> order (Optional[str]): The sorting order for the returned alphas.
> Prefix with a hyphen (-) for descending order.
> Examples: "name" (sort by name ascending), "-dateSubmitted" (sort by submission date descending).
> hidden (Optional[bool]): Filter alphas based on their visibility.
> - `True`: Only return hidden alphas.
> - `False`: Only return non-hidden alphas.
> If not provided, both hidden and non-hidden alphas are returned.
> Returns:
> Dict[str, Any]: A dictionary containing a list of alpha details under the 'results' key,
> along with pagination information. If an error occurs, it returns a dictionary with an 'error' key.
> """
> try:
> return await brain_client.get_user_alphas(
> stage=stage,
> limit=limit,
> offset=offset,
> start_date=start_date,
> end_date=end_date,
> submission_start_date=submission_start_date,
> submission_end_date=submission_end_date,
> order=order,
> hidden=hidden,
> )
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def submit_alpha(alpha_id: str) -> Dict[str, Any]:
> """
> 📤 Submit an alpha for production.
> Use this when your alpha is ready for production deployment.
> Args:
> alpha_id: The ID of the alpha to submit
> Returns:
> Submission result
> """
> try:
> success = await brain_client.submit_alpha(alpha_id)
> return {"success": success, "alpha_id": alpha_id}
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_events() -> Dict[str, Any]:
> """
> 🏆 Get available events and competitions.
> Returns:
> Available events and competitions
> """
> try:
> return await brain_client.get_events()
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_leaderboard(user_id: Optional[str] = None) -> Dict[str, Any]:
> """
> 🏅 Get leaderboard data.
> Args:
> user_id: Optional user ID to filter results
> Returns:
> Leaderboard data
> """
> try:
> return await brain_client.get_leaderboard(user_id)
> except Exception as e:
> return {"error": str(e)}
> # batch_process_alphas MCP tool removed as requested
> @mcp.tool()
> async def save_simulation_data(simulation_id: str, filename: str) -> Dict[str, Any]:
> """
> 💾 Save simulation data to a file.
> Args:
> simulation_id: The simulation ID
> filename: Filename to save the data
> Returns:
> Save operation result
> """
> try:
> # Get simulation data
> simulation_data = await brain_client.get_simulation_status(simulation_id)
> # Save to file
> with open(filename, 'w') as f:
> json.dump(simulation_data, f, indent=2)
> return {"success": True, "filename": filename, "simulation_id": simulation_id}
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_operators() -> Dict[str, Any]:
> """
> 🔧 Get available operators for alpha creation.
> Returns:
> Dictionary containing operators list and count
> """
> try:
> return await brain_client.get_operators()
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def run_selection(
> selection: str,
> instrument_type: str = "EQUITY",
> region: str = "USA",
> delay: int = 1,
> selection_limit: int = 1000,
> selection_handling: str = "POSITIVE"
> ) -> Dict[str, Any]:
> """
> 🎯 Run a selection query to filter instruments.
> Args:
> selection: Selection criteria
> instrument_type: Type of instruments
> region: Geographic region
> delay: Delay setting
> selection_limit: Maximum number of results
> selection_handling: How to handle selection results
> Returns:
> Selection results
> """
> try:
> return await brain_client.run_selection(
> selection, instrument_type, region, delay, selection_limit, selection_handling
> )
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_user_profile(user_id: str = "self") -> Dict[str, Any]:
> """
> 👤 Get user profile information.
> Args:
> user_id: User ID (default: "self" for current user)
> Returns:
> User profile data
> """
> try:
> return await brain_client.get_user_profile(user_id)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_documentations() -> Dict[str, Any]:
> """
> 📚 Get available documentations and learning materials.
> Returns:
> List of documentations
> """
> try:
> return await brain_client.get_documentations()
> except Exception as e:
> return {"error": str(e)}
> # get_messages_summary MCP tool removed as requested
> @mcp.tool()
> async def get_messages(limit: Optional[int] = None, offset: int = 0) -> Dict[str, Any]:
> """
> 💬 Get messages for the current user with optional pagination.
> Args:
> limit: Maximum number of messages to return (e.g., 10 for top 10 messages)
> Can be None (no limit), an integer, or a string that can be converted to int
> offset: Number of messages to skip (for pagination)
> Can be an integer or a string that can be converted to int
> Returns:
> Messages for the current user, optionally limited by count
> """
> try:
> # Enhanced parameter validation and conversion
> validated_limit = None
> validated_offset = 0
> # Validate and convert limit parameter
> if limit is not None:
> if isinstance(limit, str):
> if limit.strip() == "":
> # Empty string means no limit
> validated_limit = 0
> else:
> try:
> validated_limit = int(limit)
> if validated_limit < 0:
> return {"error": f"Limit must be non-negative, got: {limit}"}
> except ValueError:
> return {"error": f"Invalid limit value '{limit}'. Must be a number or empty string."}
> elif isinstance(limit, (int, float)):
> validated_limit = int(limit)
> if validated_limit < 0:
> return {"error": f"Limit must be non-negative, got: {limit}"}
> else:
> return {"error": f"Invalid limit type {type(limit).__name__}. Expected int, float, str, or None."}
> # Validate and convert offset parameter
> if isinstance(offset, str):
> try:
> validated_offset = int(offset)
> except ValueError:
> return {"error": f"Invalid offset value '{offset}'. Must be a number."}
> elif isinstance(offset, (int, float)):
> validated_offset = int(offset)
> else:
> return {"error": f"Invalid offset type {type(offset).__name__}. Expected int, float, or str."}
> if validated_offset < 0:
> return {"error": f"Offset must be non-negative, got: {offset}"}
> # Log the validated parameters for debugging
> print(f"🔍 get_messages called with validated parameters: limit={validated_limit}, offset={validated_offset}")
> # Call the brain client with validated parameters
> result = await brain_client.get_messages(validated_limit, validated_offset)
> # Add validation info to the result
> if isinstance(result, dict) and "error" not in result:
> result["_validation"] = {
> "original_limit": limit,
> "original_offset": offset,
> "validated_limit": validated_limit,
> "validated_offset": validated_offset,
> "parameter_types": {
> "limit": str(type(limit)),
> "offset": str(type(offset))
> }
> }
> return result
> except Exception as e:
> error_msg = f"get_messages failed: {str(e)}"
> print(f"❌ {error_msg}")
> return {
> "error": error_msg,
> "original_params": {
> "limit": limit,
> "offset": offset,
> "limit_type": str(type(limit)),
> "offset_type": str(type(offset))
> }
> }
> @mcp.tool()
> async def get_glossary_terms(email: str = "", password: str = "", headless: bool = False) -> Dict[str, Any]:
> """
> 📚 Get glossary terms from WorldQuant BRAIN forum.
> Note: This requires Selenium and is implemented in forum_functions.py
> Args:
> email: Your BRAIN platform email address (optional if in config)
> password: Your BRAIN platform password (optional if in config)
> headless: Run browser in headless mode (default: False)
> Returns:
> Glossary terms with definitions
> """
> try:
> # Load config to get credentials if not provided
> config = load_config()
> # Use provided credentials or fall back to config
> if not email and 'credentials' in config:
> email = config['credentials'].get('email', '')
> if not password and 'credentials' in config:
> password = config['credentials'].get('password', '')
> if not email or not password:
> return {"error": "Email and password required. Either provide them as arguments or configure them in user_config.json"}
> return await brain_client.get_glossary_terms(email, password, headless)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def search_forum_posts(search_query: str, email: str = "", password: str = "",
> max_results: int = 50, headless: bool = True) -> Dict[str, Any]:
> """
> 🔍 Search forum posts on WorldQuant BRAIN support site.
> Note: This requires Selenium and is implemented in forum_functions.py
> Args:
> email: Your BRAIN platform email address (optional if in config)
> password: Your BRAIN platform password (optional if in config)
> search_query: Search term or phrase
> max_results: Maximum number of results to return (default: 50)
> headless: Run browser in headless mode (default: True)
> Returns:
> Search results with analysis
> """
> try:
> # Load config to get credentials if not provided
> config = load_config()
> # Use provided credentials or fall back to config
> if not email and 'credentials' in config:
> email = config['credentials'].get('email', '')
> if not password and 'credentials' in config:
> password = config['credentials'].get('password', '')
> if not email or not password:
> return {"error": "Email and password required. Either provide them as arguments or configure them in user_config.json"}
> return await brain_client.search_forum_posts(email, password, search_query, max_results, headless)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def read_forum_post(article_id: str, email: str = "", password: str = "",
> headless: bool = False) -> Dict[str, Any]:
> """
> 📄 Get a specific forum post by article ID.
> Note: This requires Selenium and is implemented in forum_functions.py
> Args:
> article_id: The article ID to retrieve (e.g., "32984819083415-新人求模板")
> email: Your BRAIN platform email address (optional if in config)
> password: Your BRAIN platform password (optional if in config)
> headless: Run browser in headless mode (default: False)
> Returns:
> Forum post content with comments
> """
> try:
> # Load config to get credentials if not provided
> config = load_config()
> # Use provided credentials or fall back to config
> if not email and 'credentials' in config:
> email = config['credentials'].get('email', '')
> if not password and 'credentials' in config:
> password = config['credentials'].get('password', '')
> if not email or not password:
> return {"error": "Email and password required. Either provide them as arguments or configure them in user_config.json"}
> # Import and use forum functions directly
> from forum_functions import forum_client
> return await forum_client.read_full_forum_post(email, password, article_id, headless, include_comments=True)
> except ImportError:
> return {"error": "Forum functions require selenium. Use forum_functions.py directly."}
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_alpha_yearly_stats(alpha_id: str) -> Dict[str, Any]:
> """Get yearly statistics for an alpha."""
> try:
> return await brain_client.get_alpha_yearly_stats(alpha_id)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def check_correlation(alpha_id: str, correlation_type: str = "both", threshold: float = 0.7) -> Dict[str, Any]:
> """Check alpha correlation against production alphas, self alphas, or both."""
> try:
> return await brain_client.check_correlation(alpha_id, correlation_type, threshold)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_submission_check(alpha_id: str) -> Dict[str, Any]:
> """Comprehensive pre-submission check."""
> try:
> return await brain_client.get_submission_check(alpha_id)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def set_alpha_properties(alpha_id: str, name: Optional[str] = None,
> color: Optional[str] = None, tags: List[str] = None,
> selection_desc: str = "None", combo_desc: str = "None") -> Dict[str, Any]:
> """Update alpha properties (name, color, tags, descriptions)."""
> try:
> return await brain_client.set_alpha_properties(alpha_id, name, color, tags, selection_desc, combo_desc)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_record_sets(alpha_id: str) -> Dict[str, Any]:
> """List available record sets for an alpha."""
> try:
> return await brain_client.get_record_sets(alpha_id)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_record_set_data(alpha_id: str, record_set_name: str) -> Dict[str, Any]:
> """Get data from a specific record set."""
> try:
> return await brain_client.get_record_set_data(alpha_id, record_set_name)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_user_activities(user_id: str, grouping: Optional[str] = None) -> Dict[str, Any]:
> """Get user activity diversity data."""
> try:
> return await brain_client.get_user_activities(user_id, grouping)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_pyramid_multipliers() -> Dict[str, Any]:
> """Get current pyramid multipliers showing BRAIN's encouragement levels."""
> try:
> return await brain_client.get_pyramid_multipliers()
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_pyramid_alphas(start_date: Optional[str] = None,
> end_date: Optional[str] = None) -> Dict[str, Any]:
> """Get user's current alpha distribution across pyramid categories."""
> try:
> return await brain_client.get_pyramid_alphas(start_date, end_date)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_user_competitions(user_id: Optional[str] = None) -> Dict[str, Any]:
> """Get list of competitions that the user is participating in."""
> try:
> return await brain_client.get_user_competitions(user_id)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_competition_details(competition_id: str) -> Dict[str, Any]:
> """Get detailed information about a specific competition."""
> try:
> return await brain_client.get_competition_details(competition_id)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_competition_agreement(competition_id: str) -> Dict[str, Any]:
> """Get the rules, terms, and agreement for a specific competition."""
> try:
> return await brain_client.get_competition_agreement(competition_id)
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def get_platform_setting_options() -> Dict[str, Any]:
> """Discover valid simulation setting options (instrument types, regions, delays, universes, neutralization).
> Use this when a simulation request might contain an invalid/mismatched setting. If an AI or user supplies
> incorrect parameters (e.g., wrong region for an instrument type), call this tool to retrieve the authoritative
> option sets and correct the inputs before proceeding.
> Returns:
> A structured list of valid combinations and choice lists to validate or fix simulation settings.
> """
> try:
> return await brain_client.get_platform_setting_options()
> except Exception as e:
> return {"error": str(e)}
> @mcp.tool()
> async def performance_comparison(alpha_id: str, team_id: Optional[str] = None,
> competition: Optional[str] = None) -> Dict[str, Any]:
> """Get performance comparison data for an alpha."""
> try:
> return await brain_client.performance_comparison(alpha_id, team_id, competition)
> except Exception as e:
> return {"error": str(e)}
> # combine_test_results MCP tool removed as requested
> @mcp.tool()
> async def expand_nested_data(data: List[Dict[str, Any]], preserve_original: bool = True) -> List[Dict[str, Any]]:
> """Flatten complex nested data structures into tabular format."""
> try:
> return await brain_client.expand_nested_data(data, preserve_original)
> except Exception as e:
> return {"error": str(e)}
> # generate_alpha_links MCP tool removed as requested
> @mcp.tool()
> async def read_specific_documentation(page_id: str) -> Dict[str, Any]:
> """Retrieve detailed content of a specific documentation page/article."""
> try:
> return await brain_client.read_specific_documentation(page_id)
> except Exception as e:
> return {"error": str(e)}
> # Badge status MCP tool removed as requested
> @mcp.tool()
> async def create_multi_regularAlpha_simulation(
> alpha_expressions: List[str],
> instrument_type: str = "EQUITY",
> region: str = "USA",
> universe: str = "TOP3000",
> delay: int = 1,
> decay: float = 0.0,
> neutralization: str = "NONE",
> truncation: float = 0.0,
> test_period: str = "P0Y0M",
> unit_handling: str = "VERIFY",
> nan_handling: str = "OFF",
> language: str = "FASTEXPR",
> visualization: bool = True,
> pasteurization: str = "ON",
> max_trade: str = "OFF"
> ) -> Dict[str, Any]:
> """
> 🚀 Create multiple regular alpha simulations on BRAIN platform in a single request.
> This tool creates a multisimulation with multiple regular alpha expressions,
> waits for all simulations to complete, and returns detailed results for each alpha.
> ⏰ NOTE: Multisimulations can take 8+ minutes to complete. This tool will wait
> for the entire process and return comprehensive results.
> Call get_platform_setting_options to get the valid options for the simulation.
> Args:
> alpha_expressions: List of alpha expressions (2-8 expressions required)
> instrument_type: Type of instruments (default: "EQUITY")
> region: Market region (default: "USA")
> universe: Universe of stocks (default: "TOP3000")
> delay: Data delay (default: 1)
> decay: Decay value (default: 0.0)
> neutralization: Neutralization method (default: "NONE")
> truncation: Truncation value (default: 0.0)
> test_period: Test period (default: "P0Y0M")
> unit_handling: Unit handling method (default: "VERIFY")
> nan_handling: NaN handling method (default: "OFF")
> language: Expression language (default: "FASTEXPR")
> visualization: Enable visualization (default: True)
> pasteurization: Pasteurization setting (default: "ON")
> max_trade: Max trade setting (default: "OFF")
> Returns:
> Dictionary containing multisimulation results and individual alpha details
> """
> try:
> # Validate input
> if len(alpha_expressions) < 2:
> return {"error": "At least 2 alpha expressions are required"}
> if len(alpha_expressions) > 8:
> return {"error": "Maximum 8 alpha expressions allowed per request"}
> # Create multisimulation data
> multisimulation_data = []
> for alpha_expr in alpha_expressions:
> simulation_item = {
> 'type': 'REGULAR',
> 'settings': {
> 'instrumentType': instrument_type,
> 'region': region,
> 'universe': universe,
> 'delay': delay,
> 'decay': decay,
> 'neutralization': neutralization,
> 'truncation': truncation,
> 'pasteurization': pasteurization,
> 'unitHandling': unit_handling,
> 'nanHandling': nan_handling,
> 'language': language,
> 'visualization': visualization,
> 'testPeriod': test_period,
> 'maxTrade': max_trade
> },
> 'regular': alpha_expr
> }
> multisimulation_data.append(simulation_item)
> # Send multisimulation request
> response = brain_client.session.post(f"{brain_client.base_url}/simulations", json=multisimulation_data)
> if response.status_code != 201:
> return {"error": f"Failed to create multisimulation. Status: {response.status_code}"}
> # Get multisimulation location
> location = response.headers.get('Location', '')
> if not location:
> return {"error": "No location header in multisimulation response"}
> # Wait for children to appear and get results
> return await _wait_for_multisimulation_completion(location, len(alpha_expressions))
> except Exception as e:
> return {"error": f"Error creating multisimulation: {str(e)}"}
> async def _wait_for_multisimulation_completion(location: str, expected_children: int) -> Dict[str, Any]:
> """Wait for multisimulation to complete and return results"""
> try:
> # Simple progress indicator for users
> print(f"Waiting for multisimulation to complete... (this may take several minutes)")
> print(f"Expected {expected_children} alpha simulations")
> print()
> # Wait for children to appear - much more tolerant for 8+ minute multisimulations
> children = []
> max_wait_attempts = 200  # Increased significantly for 8+ minute multisimulations
> wait_attempt = 0
> while wait_attempt < max_wait_attempts and len(children) == 0:
> wait_attempt += 1
> try:
> multisim_response = brain_client.session.get(location)
> if multisim_response.status_code == 200:
> multisim_data = multisim_response.json()
> children = multisim_data.get('children', [])
> if children:
> break
> else:
> # Wait before next attempt - use longer intervals for multisimulations
> retry_after = multisim_response.headers.get("Retry-After", 5)
> wait_time = float(retry_after)
> await asyncio.sleep(wait_time)
> else:
> await asyncio.sleep(5)
> except Exception as e:
> await asyncio.sleep(5)
> if not children:
> return {"error": f"Children did not appear within {max_wait_attempts} attempts (multisimulation may still be processing)"}
> # Process each child to get alpha results
> alpha_results = []
> for i, child_id in enumerate(children):
> try:
> # The children are full URLs, not just IDs
> child_url = child_id if child_id.startswith('http') else f"{brain_client.base_url}/simulations/{child_id}"
> # Wait for this alpha to complete - more tolerant timing
> finished = False
> max_alpha_attempts = 100  # Increased for longer alpha processing
> alpha_attempt = 0
> while not finished and alpha_attempt < max_alpha_attempts:
> alpha_attempt += 1
> try:
> alpha_progress = brain_client.session.get(child_url)
> if alpha_progress.status_code == 200:
> alpha_data = alpha_progress.json()
> retry_after = alpha_progress.headers.get("Retry-After", 0)
> if retry_after == 0:
> finished = True
> break
> else:
> wait_time = float(retry_after)
> await asyncio.sleep(wait_time)
> else:
> await asyncio.sleep(5)
> except Exception as e:
> await asyncio.sleep(5)
> if finished:
> # Get alpha details from the completed simulation
> alpha_id = alpha_data.get("alpha")
> if alpha_id:
> # Now get the actual alpha details from the alpha endpoint
> alpha_details = brain_client.session.get(f"{brain_client.base_url}/alphas/{alpha_id}")
> if alpha_details.status_code == 200:
> alpha_detail_data = alpha_details.json()
> alpha_results.append({
> 'alpha_id': alpha_id,
> 'location': child_url,
> 'details': alpha_detail_data
> })
> else:
> alpha_results.append({
> 'alpha_id': alpha_id,
> 'location': child_url,
> 'error': f'Failed to get alpha details: {alpha_details.status_code}'
> })
> else:
> alpha_results.append({
> 'location': child_url,
> 'error': 'No alpha ID found in completed simulation'
> })
> else:
> alpha_results.append({
> 'location': child_url,
> 'error': f'Alpha simulation did not complete within {max_alpha_attempts} attempts'
> })
> except Exception as e:
> alpha_results.append({
> 'location': f"child_{i+1}",
> 'error': str(e)
> })
> # Return comprehensive results
> print(f"Multisimulation completed! Retrieved {len(alpha_results)} alpha results")
> return {
> 'success': True,
> 'message': f'Successfully created {expected_children} regular alpha simulations',
> 'total_requested': expected_children,
> 'total_created': len(alpha_results),
> 'multisimulation_id': location.split('/')[-1],
> 'multisimulation_location': location,
> 'alpha_results': alpha_results
> }
> except Exception as e:
> return {"error": f"Error waiting for multisimulation completion: {str(e)}"}
> @mcp.tool()
> async def get_daily_and_quarterly_payment(email: str = "", password: str = "") -> Dict[str, Any]:
> """
> Get daily and quarterly payment information from WorldQuant BRAIN platform.
> This function retrieves both base payments (daily alpha performance payments) and
> other payments (competition rewards, quarterly payments, referrals, etc.).
> Args:
> email: Your BRAIN platform email address (optional if in config)
> password: Your BRAIN platform password (optional if in config)
> Returns:
> Dictionary containing base payment and other payment data with summaries and detailed records
> """
> try:
> # Authenticate if credentials provided
> if email and password:
> auth_result = await brain_client.authenticate(email, password)
> if auth_result.get('status') != 'authenticated':
> return {"error": f"Authentication failed: {auth_result.get('message', 'Unknown error')}"}
> else:
> # Try to use existing session or config
> config = await manage_config("get")
> if not config.get('is_authenticated'):
> return {"error": "Not authenticated. Please provide email and password or authenticate first."}
> # Get base payment data
> base_payment_response = brain_client.session.get(
> ' [https://api.worldquantbrain.com/users/self/activities/base-payment](https://api.worldquantbrain.com/users/self/activities/base-payment) '
> )
> if base_payment_response.status_code != 200:
> return {"error": f"Failed to get base payment data: {base_payment_response.status_code}"}
> base_payment_data = base_payment_response.json()
> # Get other payment data
> other_payment_response = brain_client.session.get(
> ' [https://api.worldquantbrain.com/users/self/activities/other-payment](https://api.worldquantbrain.com/users/self/activities/other-payment) '
> )
> if other_payment_response.status_code != 200:
> return {"error": f"Failed to get other payment data: {other_payment_response.status_code}"}
> other_payment_data = other_payment_response.json()
> # Return comprehensive payment information
> return {
> "success": True,
> "base_payment": {
> "summary": {
> "yesterday": base_payment_data.get("yesterday"),
> "current_quarter": base_payment_data.get("current"),
> "previous_quarter": base_payment_data.get("previous"),
> "year_to_date": base_payment_data.get("ytd"),
> "total_all_time": base_payment_data.get("total"),
> "currency": base_payment_data.get("currency")
> },
> "daily_records": base_payment_data.get("records", {}).get("records", []),
> "schema": base_payment_data.get("records", {}).get("schema")
> },
> "other_payment": {
> "total_all_time": other_payment_data.get("total"),
> "special_payments": other_payment_data.get("records", {}).get("records", []),
> "schema": other_payment_data.get("records", {}).get("schema"),
> "currency": other_payment_data.get("currency")
> },
> "timestamp": datetime.now().isoformat()
> }
> except Exception as e:
> return {"error": f"Error retrieving payment information: {str(e)}"}
> # New MCP tool: get_error_message_fromAlphaLocation
> from typing import Sequence
> @mcp.tool()
> async def get_error_message_fromAlphaLocation(locations: Sequence[str]) -> dict:
> """
> Fetch and parse error/status from multiple simulation locations (URLs).
> Args:
> locations: List of simulation result URLs (e.g., /simulations/{id})
> Returns:
> List of dicts with location, error message, and raw response
> """
> results = []
> for loc in locations:
> try:
> resp = brain_client.session.get(loc)
> if resp.status_code != 200:
> results.append({
> "location": loc,
> "error": f"HTTP {resp.status_code}",
> "raw": resp.text
> })
> continue
> data = resp.json() if resp.text else {}
> # Try to extract error message or status
> error_msg = data.get("error") or data.get("message")
> # If alpha ID is missing, include that info
> if not data.get("alpha"):
> error_msg = error_msg or "Simulation did not get through, if you are running a multisimulation, check the other children location in your request"
> results.append({
> "location": loc,
> "error": error_msg,
> "raw": data
> })
> except Exception as e:
> results.append({
> "location": loc,
> "error": str(e),
> "raw": None
> })
> return {"results": results}
> if __name__ == "__main__":
> print("🧠 WorldQuant BRAIN MCP Server Starting...", file=sys.stderr)
> mcp.run()

```

================================================================================

B. **forum_functions.py**

```

> #!/usr/bin/env python3
> """
> WorldQuant BRAIN Forum Functions - Python Version
> Comprehensive forum functionality including glossary, search, and post viewing.
> """
> import asyncio
> import re
> import sys
> import time
> from datetime import datetime
> from typing import Dict, Any, List, Optional
> from bs4 import BeautifulSoup
> from selenium import webdriver
> from selenium.webdriver.chrome.options import Options
> from selenium.webdriver.edge.options import Options as EdgeOptions
> from selenium.webdriver.common.by import By
> from selenium.webdriver.support.ui import WebDriverWait
> from selenium.webdriver.support import expected_conditions as EC
> from selenium.common.exceptions import TimeoutException, NoSuchElementException
> import requests
> import os
> import shutil
> # Initialize forum MCP server
> try:
> from mcp.server.fastmcp import FastMCP
> forum_mcp = FastMCP('brain_forum_server')
> except ImportError:
> # Fallback for testing
> forum_mcp = None
> def log(message: str, level: str = "INFO"):
> """Log message with timestamp."""
> timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
> print(f"[{timestamp}] [{level}] {message}", file=sys.stderr)
> class ForumClient:
> """Forum client for WorldQuant BRAIN support site."""
> def __init__(self):
> self.base_url = "https://support.worldquantbrain.com"
> self.session = requests.Session()
> self.session.headers.update({
> 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
> })
> # 配置代理（从环境变量读取）
> self._configure_proxy()
> def _configure_proxy(self):
> """从多个来源配置代理设置：1)配置文件 2)环境变量 3)mcp.json"""
> try:
> http_proxy = None
> https_proxy = None
> # 1. 先尝试从用户配置文件读取
> try:
> config = self._load_config()
> proxy_config = config.get('proxy', {})
> if proxy_config.get('http'):
> http_proxy = proxy_config['http']
> log(f"从配置文件读取HTTP代理: {http_proxy}", "INFO")
> if proxy_config.get('https'):
> https_proxy = proxy_config['https']
> log(f"从配置文件读取HTTPS代理: {https_proxy}", "INFO")
> except Exception as e:
> log(f"读取配置文件代理设置失败: {str(e)}", "DEBUG")
> # 2. 如果配置文件没有，尝试从环境变量读取
> if not http_proxy:
> http_proxy = os.getenv('HTTP_PROXY') or os.getenv('http_proxy')
> if not https_proxy:
> https_proxy = os.getenv('HTTPS_PROXY') or os.getenv('https_proxy')
> # 3. 尝试从 mcp.json 读取 (如果存在)
> if not http_proxy or not https_proxy:
> try:
> mcp_config = self._load_mcp_config()
> env_vars = mcp_config.get('mcpServers', {}).get('worldquant-brain-platform', {}).get('env', {})
> if not http_proxy and env_vars.get('HTTP_PROXY'):
> http_proxy = env_vars['HTTP_PROXY']
> log(f"从mcp.json读取HTTP代理: {http_proxy}", "INFO")
> if not https_proxy and env_vars.get('HTTPS_PROXY'):
> https_proxy = env_vars['HTTPS_PROXY']
> log(f"从mcp.json读取HTTPS代理: {https_proxy}", "INFO")
> except Exception as e:
> log(f"读取mcp.json代理设置失败: {str(e)}", "DEBUG")
> # 应用代理配置
> if http_proxy or https_proxy:
> proxies = {}
> if http_proxy:
> proxies['http'] = http_proxy
> if https_proxy:
> proxies['https'] = https_proxy
> self.session.proxies.update(proxies)
> self.proxy_config = proxies
> log("代理配置已应用到requests session", "INFO")
> else:
> self.proxy_config = None
> log("未检测到任何代理设置，使用直连", "INFO")
> except Exception as e:
> log(f"代理配置失败: {str(e)}", "WARNING")
> self.proxy_config = None
> def _load_config(self):
> """加载用户配置文件（user_config.json）"""
> import json
> import sys
> from pathlib import Path
> # 尝试多个可能的配置文件位置
> config_paths = [
> "user_config.json",
> Path(__file__).parent / "user_config.json",
> Path.cwd() / "user_config.json",
> ]
> for config_path in config_paths:
> try:
> if Path(config_path).exists():
> with open(config_path, 'r', encoding='utf-8') as f:
> return json.load(f)
> except Exception as e:
> continue
> return {}
> def _load_mcp_config(self):
> """加载MCP配置文件（mcp.json）"""
> import json
> from pathlib import Path
> # 尝试多个可能的mcp.json位置
> mcp_paths = [
> "mcp.json",
> Path(__file__).parent / "mcp.json",
> Path.cwd() / "mcp.json",
> Path.home() / ".cursor" / "mcp.json",  # Cursor默认位置
> ]
> for mcp_path in mcp_paths:
> try:
> if Path(mcp_path).exists():
> with open(mcp_path, 'r', encoding='utf-8') as f:
> return json.load(f)
> except Exception as e:
> continue
> return {}
> def get_brain_session(self):
> """Get authenticated session from BrainApiClient."""
> try:
> import sys
> import os
> sys.path.append(os.path.dirname(os.path.abspath(__file__)))
> from platform_functions import brain_client
> return brain_client.session
> except ImportError:
> return None
> def detect_available_browser(self) -> str:
> """Detect which browser WebDriver is available."""
> try:
> # Try Chrome first
> from selenium.webdriver.chrome.service import Service
> from selenium.webdriver.chrome.options import Options
> try:
> options = Options()
> options.add_argument('--headless')
> driver = webdriver.Chrome(options=options)
> driver.quit()
> return "chrome"
> except Exception:
> pass
> # Try Edge
> try:
> from selenium.webdriver.edge.options import Options as EdgeOptions
> options = EdgeOptions()
> options.add_argument('--headless')
> driver = webdriver.Edge(options=options)
> driver.quit()
> return "edge"
> except Exception:
> pass
> # Default to chrome
> return "chrome"
> except Exception:
> return "chrome"
> def setup_browser_options(self, headless: bool, browser_type: str):
> """Setup browser options based on browser type."""
> if browser_type.lower() == "chrome":
> return self.setup_chrome_options(headless)
> elif browser_type.lower() == "edge":
> return self.setup_edge_options(headless)
> else:
> return self.setup_chrome_options(headless)
> def setup_edge_options(self, headless: bool = True) -> EdgeOptions:
> """Setup Edge options for web scraping."""
> options = EdgeOptions()
> if headless:
> options.add_argument('--headless')
> # 代理配置
> if hasattr(self, 'proxy_config') and self.proxy_config:
> # 使用HTTP代理或HTTPS代理
> proxy_url = self.proxy_config.get('http') or self.proxy_config.get('https')
> if proxy_url:
> options.add_argument(f'--proxy-server={proxy_url}')
> log(f"Edge WebDriver配置代理: {proxy_url}", "INFO")
> # Performance optimizations
> options.add_argument('--disable-blink-features=AutomationControlled')
> options.add_argument('--log-level=3')
> options.add_argument('--no-sandbox')
> options.add_argument('--disable-dev-shm-usage')
> options.add_argument('--disable-web-security')
> options.add_argument('--disable-features=VizDisplayCompositor')
> options.add_argument('--disable-gpu')
> options.add_argument('--disable-extensions')
> options.add_argument('--disable-images')
> options.add_argument('--disable-javascript')
> options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36')
> return options
> def setup_chrome_options(self, headless: bool = True) -> Options:
> """Setup Chrome options for web scraping."""
> options = Options()
> if headless:
> options.add_argument('--headless')
> # 代理配置
> if hasattr(self, 'proxy_config') and self.proxy_config:
> # 使用HTTP代理或HTTPS代理
> proxy_url = self.proxy_config.get('http') or self.proxy_config.get('https')
> if proxy_url:
> options.add_argument(f'--proxy-server={proxy_url}')
> log(f"Chrome WebDriver配置代理: {proxy_url}", "INFO")
> # Performance optimizations
> options.add_argument('--disable-blink-features=AutomationControlled')
> options.add_argument('--log-level=3')
> options.add_argument('--no-sandbox')
> options.add_argument('--disable-dev-shm-usage')
> options.add_argument('--disable-web-security')
> options.add_argument('--disable-features=VizDisplayCompositor')
> options.add_argument('--disable-gpu')
> options.add_argument('--disable-extensions')
> options.add_argument('--disable-images')
> options.add_argument('--disable-javascript')
> options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36')
> return options
> async def create_driver(self, headless: bool = True):
> """Create and configure WebDriver with cross-browser support."""
> browser_type = self.detect_available_browser()
> log(f"Using browser: {browser_type}", "INFO")
> options = self.setup_browser_options(headless, browser_type)
> try:
> if browser_type.lower() == "chrome":
> driver = webdriver.Chrome(options=options)
> elif browser_type.lower() == "edge":
> driver = webdriver.Edge(options=options)
> else:
> # Fallback to Chrome
> log("Falling back to Chrome", "WARNING")
> driver = webdriver.Chrome(options=options)
> # Set aggressive timeouts for speed
> driver.set_page_load_timeout(30)
> driver.implicitly_wait(10)
> return driver
> except Exception as e:
> log(f"Failed to create {browser_type} driver: {str(e)}", "ERROR")
> help_text = self.get_driver_installation_help(browser_type)
> log(help_text, "ERROR")
> # Try Chrome as fallback if Edge failed
> if browser_type.lower() != "chrome":
> try:
> log("Trying Chrome as fallback", "INFO")
> chrome_options = self.setup_browser_options(headless, "chrome")
> driver = webdriver.Chrome(options=chrome_options)
> driver.set_page_load_timeout(30)
> driver.implicitly_wait(10)
> return driver
> except Exception as e2:
> log(f"Chrome fallback also failed: {str(e2)}", "ERROR")
> chrome_help = self.get_driver_installation_help("chrome")
> log(chrome_help, "ERROR")
> raise Exception(f"Could not create any browser driver. {help_text}")
> async def login_to_forum(self, driver, email: str, password: str) -> bool:
> """Login to the WorldQuant BRAIN forum using existing authentication."""
> try:
> # Import BrainApiClient from platform_functions
> import sys
> import os
> sys.path.append(os.path.dirname(os.path.abspath(__file__)))
> try:
> from platform_functions import brain_client
> log("Using existing BrainApiClient for authentication", "INFO")
> # First authenticate with BrainApiClient
> auth_result = await brain_client.authenticate(email, password)
> if auth_result.get('status') != 'authenticated':
> log("BrainApiClient authentication failed", "ERROR")
> return False
> log("Successfully authenticated via BrainApiClient", "SUCCESS")
> # Navigate to forum with authenticated session
> log("Navigating to forum with authenticated session", "WORK")
> driver.get(" [https://support.worldquantbrain.com/hc/en-us](/hc/en-us) ")
> await asyncio.sleep(2)
> # Add authentication cookies to browser
> cookies = brain_client.session.cookies
> for cookie in cookies:
> driver.add_cookie({
> 'name': cookie.name,
> 'value': cookie.value,
> 'domain': '.worldquantbrain.com'
> })
> # Refresh page with cookies
> driver.refresh()
> await asyncio.sleep(2)
> return True
> except ImportError:
> log("BrainApiClient not available, using manual login", "WARNING")
> # Fallback to manual login
> driver.get(" [https://support.worldquantbrain.com/hc/en-us/signin](/hc/en-us/signin) ")
> await asyncio.sleep(3)
> email_input = WebDriverWait(driver, 15).until(
> EC.presence_of_element_located((By.NAME, "email"))
> )
> password_input = WebDriverWait(driver, 15).until(
> EC.presence_of_element_located((By.NAME, "currentPassword"))
> )
> email_input.clear()
> email_input.send_keys(email)
> password_input.clear()
> password_input.send_keys(password)
> login_button = WebDriverWait(driver, 15).until(
> EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
> )
> login_button.click()
> await asyncio.sleep(3)
> return True
> except Exception as e:
> log(f"Login failed: {str(e)}", "ERROR")
> return False
> async def get_glossary_terms(self, email: str, password: str, headless: bool = False) -> Dict[str, Any]:
> """Extract glossary terms from the forum."""
> driver = None
> try:
> log("Starting glossary extraction process", "INFO")
> # Add timeout protection
> async def extraction_with_timeout():
> return await self._perform_glossary_extraction(email, password, headless)
> # Run with 5-minute timeout
> result = await asyncio.wait_for(extraction_with_timeout(), timeout=300)
> return result
> except asyncio.TimeoutError:
> log("Glossary extraction timed out after 5 minutes", "ERROR")
> return {"error": "Glossary extraction timed out after 5 minutes"}
> except Exception as e:
> log(f"Glossary extraction failed: {str(e)}", "ERROR")
> return {"error": str(e)}
> finally:
> if driver:
> try:
> driver.quit()
> except:
> pass
> async def _perform_glossary_extraction(self, email: str, password: str, headless: bool) -> Dict[str, Any]:
> """Perform the actual glossary extraction."""
> driver = None
> try:
> driver = await self.create_driver(headless)
> # Login
> if not await self.login_to_forum(driver, email, password):
> raise Exception("Failed to login to forum")
> # Navigate to glossary page
> log("Navigating to glossary page", "WORK")
> driver.get(" [https://support.worldquantbrain.com/hc/en-us/articles/4902349883927-Click-here-for-a-list-of-terms-and-their-definitions](/hc/en-us/articles/4902349883927-Click-here-for-a-list-of-terms-and-their-definitions) ")
> await asyncio.sleep(5)
> # Extract content
> log("Extracting glossary content", "WORK")
> page_source = driver.page_source
> soup = BeautifulSoup(page_source, 'html.parser')
> # Parse glossary terms
> terms = self._parse_glossary_terms(page_source)
> log(f"Extracted {len(terms)} glossary terms", "SUCCESS")
> return {
> "terms": terms,
> "total_count": len(terms),
> "extraction_timestamp": datetime.now().isoformat()
> }
> finally:
> if driver:
> try:
> driver.quit()
> except:
> pass
> def _parse_glossary_terms(self, content: str) -> List[Dict[str, str]]:
> """Parse glossary terms from HTML content."""
> terms = []
> lines = content.split('\n')
> current_term = None
> current_definition = []
> is_collecting_definition = False
> found_first_real_term = False
> for line in lines:
> line = line.strip()
> if not line:
> continue
> # Skip navigation and metadata lines at the beginning
> if not found_first_real_term and self._is_navigation_or_metadata(line):
> continue
> # Check if this line looks like a term
> if self._looks_like_term(line) and not is_collecting_definition:
> # Mark that we found the first real term
> if not found_first_real_term:
> found_first_real_term = True
> # Save previous term if exists
> if current_term and current_definition:
> terms.append({
> "term": current_term.strip(),
> "definition": " ".join(current_definition).strip()
> })
> current_term = line
> current_definition = []
> is_collecting_definition = True
> elif is_collecting_definition and found_first_real_term:
> # Check if this is the start of a new term
> if self._looks_like_term(line):
> # Save current term
> if current_term and current_definition:
> terms.append({
> "term": current_term.strip(),
> "definition": " ".join(current_definition).strip()
> })
> current_term = line
> current_definition = []
> else:
> # Add to definition
> if current_definition:
> current_definition.append(line)
> else:
> current_definition = [line]
> # Don't forget the last term
> if current_term and current_definition and found_first_real_term:
> terms.append({
> "term": current_term.strip(),
> "definition": " ".join(current_definition).strip()
> })
> # Filter out invalid terms and improve quality
> return[term for term in terms if
> len(term["term"])>0and
> len(term["definition"]) > 10 and  # Ensure meaningful definitions
> not self._is_navigation_or_metadata(term["term"]) and
> "ago" not in term["definition"] and  # Remove timestamp-like definitions
> "minute read" not in term["definition"]]  # Remove reading time
> def _looks_like_term(self, line: str) -> bool:
> """Check if a line looks like a glossary term."""
> # Skip very long lines (likely definitions)
> if len(line) > 100:
> return False
> # Skip navigation and metadata
> if self._is_navigation_or_metadata(line):
> return False
> # Skip lines that start with common definition words
> definition_starters = ['the', 'a', 'an', 'this', 'that', 'it', 'is', 'are', 'was', 'were', 'for', 'to', 'in', 'on', 'at', 'by', 'with']
> first_word = line.lower().split(' ')[0]
> if first_word and first_word in definition_starters:
> return False
> # Check if line has characteristics of a term
> # Terms are often short, may be all caps, or start with capital
> is_short = len(line) <= 80
> starts_with_capital = bool(re.match(r'^[A-Z]', line))
> has_all_caps = bool(re.match(r'^[A-Z\s\-\/]+$', line))
> has_reasonable_length = len(line) >= 2
> return is_short and has_reasonable_length and (starts_with_capital or has_all_caps)
> def _is_navigation_or_metadata(self, line: str) -> bool:
> """Check if a line is navigation or metadata."""
> navigation_patterns = [
> r'^\d+ days? ago$',
> r'~\d+ minute read',
> r'^Follow',
> r'^Not yet followed',
> r'^Updated$',
> r'^AS\d+$',
> r'^[A-Z] - [A-Z] - [A-Z]',  # Letter navigation
> r'^A$',
> r'^B$',
> r'^[A-Z]$'  # Single letters
> ]
> return any(re.match(pattern, line.strip()) for pattern in navigation_patterns)
> def get_driver_installation_help(self, browser_type: str) -> str:
> """Provide helpful instructions for installing WebDriver."""
> if browser_type.lower() == "chrome":
> return """
> Chrome WebDriver not found. Please install ChromeDriver:
> 1. Download from:  [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
> 2. Make sure version matches your Chrome browser
> 3. Add to PATH or place in current directory
> 4. Alternative: Install via pip: pip install chromedriver-autoinstaller
> """
> elif browser_type.lower() == "edge":
> return """
> Edge WebDriver not found. Please install Edge WebDriver:
> 1. Download from:  [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
> 2. Make sure version matches your Edge browser
> 3. Add to PATH or place in current directory
> 4. Alternative: Install via pip: pip install msedge-selenium-tools
> """
> else:
> return "Please install either ChromeDriver or Edge WebDriver for browser automation."
> asyncdefread_full_forum_post(self,email:str,password:str,post_url_or_id:str,
> headless: bool = False, include_comments: bool = True) -> Dict[str, Any]:
> """Read a complete forum post with optional comments."""
> driver = None
> try:
> log("Starting forum post reading process", "INFO")
> # Determine if input is URL or article ID
> is_url = post_url_or_id.startswith('http')
> if is_url:
> post_url = post_url_or_id
> else:
> post_url = f" [https://support.worldquantbrain.com/hc/zh-cn/community/posts/{post_url_or_id}](/hc/zh-cn/community/posts/{post_url_or_id}) "
> log(f"Target URL: {post_url}", "INFO")
> log(f"Include comments: {include_comments}", "INFO")
> driver = await self.create_driver(headless)
> # Login
> if not await self.login_to_forum(driver, email, password):
> raise Exception("Failed to login to forum")
> # Navigate directly to post URL
> log(f"Opening post: {post_url}", "WORK")
> driver.get(post_url)
> log("Post page loaded, extracting content immediately", "WORK")
> # Wait minimal time for content to appear
> await asyncio.sleep(2)
> # Extract post content quickly
> post_data = {}
> page_source = driver.page_source
> soup = BeautifulSoup(page_source, 'html.parser')
> # Extract post title
> title = soup.select_one('.post-title, h1, .article-title')
> if not title:
> title = soup.select_one('title')
> post_data['title'] = title.get_text().strip() if title else 'Unknown Title'
> # Extract post author
> author = soup.select_one('.post-author, .author, .article-author')
> if not author:
> author = soup.select_one('.comment-author')
> post_data['author'] = author.get_text().strip() if author else 'Unknown Author'
> # Extract post date
> date = soup.select_one('.post-date, .date, .article-date, time')
> if not date:
> time_element = soup.select_one('time')
> if time_element:
> date = time_element.get('datetime') or time_element.get('title') or time_element.get_text().strip()
> else:
> date = 'Unknown Date'
> else:
> date = date.get_text().strip()
> post_data['date'] = date if date else 'Unknown Date'
> # Extract post content
> post_content = soup.select_one('.post-body, .article-body, .content, .post-content')
> if not post_content:
> post_content = soup.select_one('article, main')
> if post_content:
> post_data['content_html'] = str(post_content)
> post_data['content_text'] = post_content.get_text().strip()
> else:
> post_data['content_html'] = 'No content found'
> post_data['content_text'] = 'No content found'
> post_data['url'] = post_url
> post_data['current_url'] = driver.current_url
> log(f"Post content extracted: \"{post_data['title']}\"", "SUCCESS")
> comments = []
> total_comments = 0
> # Extract comments conditionally
> if include_comments:
> log("Extracting comments...", "WORK")
> comments = await self._extract_forum_comments_full(driver, soup)
> total_comments = len(comments)
> log(f"Extracted {total_comments} comments", "SUCCESS")
> else:
> log("Skipping comment extraction (includeComments=false)", "INFO")
> return {
> "success": True,
> "post": post_data,
> "comments": comments,
> "total_comments": total_comments,
> "extracted_at": datetime.now().isoformat(),
> "processing_time": "full_extraction_with_comments" if include_comments else "post_only_extraction",
> "include_comments": include_comments
> }
> except Exception as e:
> log(f"Failed to read forum post: {str(e)}", "ERROR")
> return {"error": str(e)}
> finally:
> if driver:
> try:
> driver.quit()
> except:
> pass
> async def _extract_forum_comments_full(self, driver, soup: BeautifulSoup) -> List[Dict[str, Any]]:
> """Extract all comments from forum post with pagination support."""
> all_comments = []
> page_num = 1
> try:
> # First extract comments from current page source
> page_comments = self._parse_comments_from_html(soup)
> all_comments.extend(page_comments)
> log(f"Found {len(page_comments)} comments on page {page_num}", "INFO")
> # Check for pagination and continue if needed
> while True:
> try:
> # Look for next page button
> next_button = driver.find_element(By.CSS_SELECTOR, "span.pagination-next-text, .pagination-next, .next")
> next_text = next_button.text
> if "下一页" in next_text or "Next" in next_text or "next" in next_text.lower():
> log(f"Found next page, continuing to page {page_num + 1}", "INFO")
> next_button.click()
> await asyncio.sleep(2)  # Minimal wait for next page
> # Extract comments from new page
> new_page_source = driver.page_source
> new_soup = BeautifulSoup(new_page_source, 'html.parser')
> new_page_comments = self._parse_comments_from_html(new_soup)
> if len(new_page_comments) == 0:
> break
> all_comments.extend(new_page_comments)
> page_num += 1
> log(f"Found {len(new_page_comments)} comments on page {page_num}", "INFO")
> else:
> break
> except Exception as e:
> log("No more pages found", "INFO")
> break
> return all_comments
> except Exception as e:
> log(f"Error in comment extraction: {str(e)}", "WARNING")
> return all_comments
> def _parse_comments_from_html(self, soup: BeautifulSoup) -> List[Dict[str, Any]]:
> """Parse comments from HTML using BeautifulSoup."""
> comments = []
> # Try multiple selectors for comments
> comment_selectors = [
> 'ul#comments.comment-list li.comment',
> '.comment-list .comment',
> '.comments .comment',
> 'li.comment',
> '.comment-item'
> ]
> comment_elements = None
> for selector in comment_selectors:
> comment_elements = soup.select(selector)
> if comment_elements:
> log(f"Found comments using selector: {selector}", "INFO")
> break
> if not comment_elements:
> log("No comments found on this page", "INFO")
> return comments
> for index, element in enumerate(comment_elements):
> try:
> comment = {}
> # Extract comment ID
> comment['id'] = element.get('id') or f"comment-{index}"
> # Extract author
> author_element = element.select_one('.comment-author a, .author a, .comment-author')
> comment['author'] = author_element.get_text().strip() if author_element else 'Unknown Author'
> comment['author_link'] = author_element.get('href') if author_element else ''
> # Extract date
> time_element = element.select_one('.meta-data time, time, .date, .comment-date')
> if time_element:
> comment['date'] = time_element.get('datetime') or time_element.get('title') or time_element.get_text().strip()
> comment['date_display'] = time_element.get('title') or time_element.get_text().strip()
> else:
> comment['date'] = 'Unknown Date'
> comment['date_display'] = 'Unknown Date'
> # Extract content
> content_element = element.select_one('.comment-body, .comment-content, .content')
> if content_element:
> comment['content_html'] = str(content_element)
> comment['content_text'] = content_element.get_text().strip()
> else:
> comment['content_html'] = ''
> comment['content_text'] = ''
> # Extract votes
> vote_element = element.select_one('.vote-up span, .votes, .vote-count')
> comment['votes'] = vote_element.get_text().strip() if vote_element else '0'
> # Extract status
> status_element = element.select_one('.status-label, .status, .badge')
> comment['status'] = status_element.get_text().strip() if status_element else '普通评论'
> if comment['content_text']:
> comments.append(comment)
> except Exception as e:
> log(f"Error parsing comment {index}: {str(e)}", "WARNING")
> return comments
> asyncdefsearch_forum_posts(self,email:str,password:str,search_query:str,
> max_results: int = 50, headless: bool = True) -> Dict[str, Any]:
> """Search forum posts."""
> driver = None
> try:
> log("Starting forum search process", "INFO")
> log(f"Search query: '{search_query}'", "INFO")
> log(f"Max results: {max_results}", "INFO")
> driver = await self.create_driver(headless)
> # Login
> if not await self.login_to_forum(driver, email, password):
> raise Exception("Failed to login to forum")
> # Navigate to search
> encoded_query = requests.utils.quote(search_query)
> search_url = f" [https://support.worldquantbrain.com/hc/zh-cn/search?utf8=%E2%9C%93&query={encoded_query}](/hc/zh-cn/search?utf8=%E2%9C%93&query={encoded_query}) "
> log(f"Opening search URL: {search_url}", "WORK")
> driver.get(search_url)
> await asyncio.sleep(2)
> # Collect results with pagination
> all_results = []
> page_num = 1
> log("Starting result collection with pagination", "WORK")
> while len(all_results) < max_results:
> log(f"Processing page {page_num}", "INFO")
> # Wait for search results
> try:
> WebDriverWait(driver, 10).until(
> EC.presence_of_element_located((By.CSS_SELECTOR, '.search-results-list, .search-result-list-item'))
> )
> except TimeoutException:
> log(f"No search results found on page {page_num}", "WARNING")
> break
> # Extract results from current page
> page_source = driver.page_source
> soup = BeautifulSoup(page_source, 'html.parser')
> page_results = self._extract_search_results(soup, page_num)
> if not page_results:
> log(f"No more results found on page {page_num}", "INFO")
> break
> all_results.extend(page_results)
> # Check if we have enough results
> if len(all_results) >= max_results:
> all_results = all_results[:max_results]
> break
> # Try to go to next page
> if not await self._go_to_next_search_page(driver, soup):
> log("No more pages available", "INFO")
> break
> page_num += 1
> await asyncio.sleep(1)
> # Analyze results
> analysis = self._analyze_search_results(all_results, search_query)
> log(f"Search completed. Found {len(all_results)} results", "SUCCESS")
> return {
> "results": all_results,
> "total_found": len(all_results),
> "search_query": search_query,
> "analysis": analysis,
> "search_timestamp": datetime.now().isoformat()
> }
> except Exception as e:
> log(f"Search failed: {str(e)}", "ERROR")
> return {"error": str(e)}
> finally:
> if driver:
> try:
> driver.quit()
> except:
> pass
> def _extract_search_results(self, soup: BeautifulSoup, page_num: int) -> List[Dict[str, Any]]:
> """Extract search results from a page using multiple resilient selectors.
> Improvements vs original implementation:
> - Tries several container selectors (mirrors TS Cheerio approach)
> - Extracts richer metadata: description_html/text, votes, comments, author, date
> - Preserves legacy fields (snippet, metadata) for backward compatibility
> - Adds index & page for downstream analytics
> - Robust fallbacks & normalization of URLs
> """
> results: List[Dict[str, Any]] = []
> # Ordered list of possible container selectors (keep broad ones last)
> container_selectors = [
> '.search-result-list-item',
> '.search-results-list .search-result',
> '.striped-list-item',
> '.article-list-item',
> 'article.search-result',
> 'div.search-result',
> ]
> # Collect candidate elements (stop at first selector that yields results)
> result_items = []
> for selector in container_selectors:
> found = soup.select(selector)
> if found:
> log(f"Found {len(found)} search results using selector: {selector}", "INFO")
> result_items = found
> break
> # Fallback: regex class scan (original heuristic)
> if not result_items:
> fallback = soup.find_all(['article', 'div'], class_=re.compile(r'search-result|article-item'))
> if fallback:
> log(f"Fallback selector captured {len(fallback)} results", "INFO")
> result_items = fallback
> else:
> log("No search result items found with any selector", "WARNING")
> return results
> def first_text(element, selector_list: List[str]) -> str:
> for sel in selector_list:
> found = element.select_one(sel)
> if found and found.get_text(strip=True):
> return found.get_text(strip=True)
> return ''
> for idx, item in enumerate(result_items):
> try:
> # Title & link
> title_link_elem = None
> title_selectors = [
> '.search-result-title a',
> 'h3 a',
> '.title a',
> 'a'
> ]
> for sel in title_selectors:
> candidate = item.select_one(sel)
> if candidate and candidate.get_text(strip=True):
> title_link_elem = candidate
> break
> title = title_link_elem.get_text(strip=True) if title_link_elem else 'No title'
> link = title_link_elem.get('href') if title_link_elem and title_link_elem.has_attr('href') else ''
> if link and not link.startswith('http'):
> link = f" [https://support.worldquantbrain.com{link}](https://support.worldquantbrain.com{link}) "
> if not link and not title:
> continue  # Skip invalid entries
> # Description / snippet
> desc_elem = None
> desc_selectors = [
> '.search-results-description',
> '.description',
> '.excerpt',
> '.content-preview',
> 'p'
> ]
> for sel in desc_selectors:
> candidate = item.select_one(sel)
> if candidate and candidate.get_text(strip=True):
> desc_elem = candidate
> break
> description_html = str(desc_elem) if desc_elem else ''
> description_text = desc_elem.get_text(strip=True) if desc_elem else ''
> # Votes & comments
> votes = first_text(item, [
> '.search-result-votes span',
> '.votes span',
> '[class*="vote"] span',
> '[class*="vote"]'
> ]) or '0'
> comments = first_text(item, [
> '.search-result-meta-count span',
> '.comments span',
> '[class*="comment"] span',
> '[class*="comment"]'
> ]) or '0'
> # Metadata / author / date
> meta_block = item.select_one('.meta-data, .metadata, .post-meta')
> author = 'Unknown'
> date_val = 'Unknown'
> if meta_block:
> meta_text = meta_block.get_text(' ', strip=True)
> # Split on common separators
> parts = [p.strip() for p in re.split(r'[·•|]', meta_text) if p.strip()]
> if len(parts) >= 2:
> author = parts[0] or author
> date_val = parts[1] or date_val
> # Fallback selectors
> if author == 'Unknown':
> author = first_text(item, ['.author', '.username', '[class*="author"]']) or 'Unknown'
> if date_val == 'Unknown':
> # time element or date class
> time_elem = item.select_one('.date, time, [class*="date"]')
> if time_elem:
> date_val = time_elem.get('datetime') or time_elem.get('title') or time_elem.get_text(strip=True) or 'Unknown'
> # Compose legacy fields
> snippet = description_text
> metadata = f"author={author} date={date_val} votes={votes} comments={comments}".strip()
> results.append({
> 'title': title,
> 'link': link,
> 'description_html': description_html or 'No description',
> 'description_text': description_text or 'No description',
> 'votes': votes,
> 'comments': comments,
> 'author': author,
> 'date': date_val,
> 'snippet': snippet,      # backward compatibility
> 'metadata': metadata,    # backward compatibility / quick summary
> 'page': page_num,
> 'index': idx
> })
> except Exception as e:
> log(f"Error extracting search result {idx}: {str(e)}", "WARNING")
> continue
> return results
> async def _go_to_next_search_page(self, driver: webdriver.Chrome, soup: BeautifulSoup) -> bool:
> """Navigate to the next search page."""
> try:
> # Look for next page link
> next_link = soup.find('a', string=re.compile(r'next|下一页', re.IGNORECASE))
> if not next_link:
> next_link = soup.find('a', {'rel': 'next'})
> if next_link and next_link.get('href'):
> next_url = next_link['href']
> if not next_url.startswith('http'):
> next_url = f" [https://support.worldquantbrain.com{next_url}](https://support.worldquantbrain.com{next_url}) "
> driver.get(next_url)
> await asyncio.sleep(2)
> return True
> return False
> except Exception as e:
> log(f"Error navigating to next page: {str(e)}", "WARNING")
> return False
> def _analyze_search_results(self, results: List[Dict[str, Any]], search_query: str) -> Dict[str, Any]:
> """Analyze search results for insights."""
> if not results:
> return {"message": "No results found"}
> # Basic statistics
> total_results = len(results)
> # Categorize results by type
> categories = {}
> for result in results:
> title = result.get('title', '').lower()
> if 'tutorial' in title or 'guide' in title:
> categories['tutorials'] = categories.get('tutorials', 0) + 1
> elif 'api' in title or 'reference' in title:
> categories['api_docs'] = categories.get('api_docs', 0) + 1
> elif 'error' in title or 'issue' in title or 'problem' in title:
> categories['troubleshooting'] = categories.get('troubleshooting', 0) + 1
> elif 'competition' in title or 'event' in title:
> categories['competitions'] = categories.get('competitions', 0) + 1
> else:
> categories['general'] = categories.get('general', 0) + 1
> # Find most relevant results (containing search terms)
> search_terms = search_query.lower().split()
> relevant_results = []
> for result in results:
> title = result.get('title', '').lower()
> snippet = result.get('snippet', '').lower()
> text = f"{title} {snippet}"
> term_matches = sum(1 for term in search_terms if term in text)
> if term_matches > 0:
> relevant_results.append({
> "result": result,
> "relevance_score": term_matches / len(search_terms)
> })
> # Sort by relevance
> relevant_results.sort(key=lambda x: x['relevance_score'], reverse=True)
> return {
> "total_results": total_results,
> "categories": categories,
> "most_relevant": relevant_results[:5] if relevant_results else [],
> "search_terms": search_terms
> }
> # Initialize forum client
> forum_client = ForumClient()
> # MCP Tools for Forum Functions - REMOVED (duplicate with platform_functions.py)
> # These tools are already properly integrated in the main platform_functions.py
> if __name__ == "__main__":
> print("📚 WorldQuant BRAIN Forum Functions Server Starting...", file=sys.stderr)
> print("Note: Forum tools are now integrated in the main platform_functions.py", file=sys.stderr)
> print("This file provides the ForumClient class for internal use.",file=sys.stderr)

```

2.mcp.json修改

```

> {
> "mcpServers": {
> "worldquant-brain-platform": {
> "command": "C:\Users\此处写python.exe的绝对路径\Python\Python310\python.exe",
> "args": ["C:\Users\此处写platform_functions.py的绝对路径\Programs\Python\Python310\Lib\site-packages\cnhkmcp\untracked\platform_functions.py"],
> "description": "WorldQuant BRAIN Platform MCP Server - Comprehensive trading platform integration with simulation management, alpha operations, and authentication. Credentials are stored in user_config.json in the same directory. Provides tools for creating simulations, checking status, managing alphas, and accessing platform features.",
> "env": {
> "HTTP_PROXY": " [http://127.0.0.1:7890](http://127.0.0.1:7890) ",
> "HTTPS_PROXY": " [http://127.0.0.1:7890](http://127.0.0.1:7890) ",
> "NO_PROXY": "localhost,127.0.0.1",
> "PYTHONHTTPSVERIFY": "0",
> "CURL_CA_BUNDLE": "",
> "REQUESTS_CA_BUNDLE": ""
> }
> }
> }
> }

```

此处代理端口设置为7890

---

## 讨论与评论 (4)

### 评论 #1 (作者: YL20168, 时间: 10 months ago)

太赞了，原本一直连接不上mcp，用了这个方法果然有效

---

### 评论 #2 (作者: ZZ37826, 时间: 10 months ago)

嗯嗯，原理上就是cnhkmcp的写在代码里的mcp网络请求并没有设置代理，这个修改后的代码就是把API的代理给加上了。

---

### 评论 #3 (作者: TB73554, 时间: 9 months ago)

感谢，看了这篇帖子，终于连接成功了

---

### 评论 #4 (作者: YQ84572, 时间: 6 months ago)

感谢分享，看完帖子也是终于解决了mcp连不上论坛的问题，曾经困扰很久了。
=======================================================================================================================================================================

---

