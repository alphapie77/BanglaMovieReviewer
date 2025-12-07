@echo off
cd frontend
if not exist node_modules npm install
echo Frontend: http://localhost:3000
npm start
