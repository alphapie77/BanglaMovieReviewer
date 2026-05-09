import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

export const getModels = async () => {
  const response = await axios.get(`${API_BASE_URL}/sentiment/models/`);
  return response.data;
};

export const analyzeSentiment = async (reviewText, modelName = 'BanglaBERT') => {
  const response = await axios.post(`${API_BASE_URL}/sentiment/analyze/`, {
    review_text: reviewText,
    model_name: modelName
  });
  return response.data;
};

export const getHistory = async () => {
  const response = await axios.get(`${API_BASE_URL}/sentiment/history/`);
  return response.data;
};
