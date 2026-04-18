// ========================================
// NextGen Dev - API Client
// ========================================

const API_BASE_URL = window.location.hostname === 'localhost' 
  ? 'http://localhost:5000/api' 
  : '/api';

class API {
  static async request(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`;
    
    const config = {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers
      },
      ...options
    };
    
    // Add auth token if available
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    
    if (config.body && typeof config.body === 'object' && !(config.body instanceof FormData)) {
      config.body = JSON.stringify(config.body);
    }
    
    try {
      const response = await fetch(url, config);
      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.error || `HTTP ${response.status}`);
      }
      
      return data;
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  }
  
  // Auth
  static async login(email, password) {
    return this.request('/auth/login', {
      method: 'POST',
      body: { email, password }
    });
  }
  
  static async register(email, password, name) {
    return this.request('/auth/register', {
      method: 'POST',
      body: { email, password, name }
    });
  }
  
  static async getMe() {
    return this.request('/auth/me');
  }
  
  // Portfolios
  static async getPortfolios(category) {
    const query = category ? `?category=${encodeURIComponent(category)}` : '';
    return this.request(`/portfolios${query}`);
  }
  
  static async getPortfolio(id) {
    return this.request(`/portfolios/${id}`);
  }
  
  static async createPortfolio(data) {
    return this.request('/portfolios', { method: 'POST', body: data });
  }
  
  static async updatePortfolio(id, data) {
    return this.request(`/portfolios/${id}`, { method: 'PUT', body: data });
  }
  
  static async deletePortfolio(id) {
    return this.request(`/portfolios/${id}`, { method: 'DELETE' });
  }
  
  // Gallery
  static async getGallery(category) {
    const query = category ? `?category=${encodeURIComponent(category)}` : '';
    return this.request(`/gallery${query}`);
  }
  
  static async createGalleryImage(data) {
    return this.request('/gallery', { method: 'POST', body: data });
  }
  
  static async updateGalleryImage(id, data) {
    return this.request(`/gallery/${id}`, { method: 'PUT', body: data });
  }
  
  static async deleteGalleryImage(id) {
    return this.request(`/gallery/${id}`, { method: 'DELETE' });
  }
  
  // Events
  static async getEvents(status) {
    const query = status ? `?status=${encodeURIComponent(status)}` : '';
    return this.request(`/events${query}`);
  }
  
  static async createEvent(data) {
    return this.request('/events', { method: 'POST', body: data });
  }
  
  static async updateEvent(id, data) {
    return this.request(`/events/${id}`, { method: 'PUT', body: data });
  }
  
  static async deleteEvent(id) {
    return this.request(`/events/${id}`, { method: 'DELETE' });
  }
  
  // Blog
  static async getBlogPosts(status, category) {
    const params = new URLSearchParams();
    if (status) params.append('status', status);
    if (category) params.append('category', category);
    const query = params.toString() ? `?${params.toString()}` : '';
    return this.request(`/blog${query}`);
  }
  
  static async getBlogPost(id) {
    return this.request(`/blog/${id}`);
  }
  
  static async createBlogPost(data) {
    return this.request('/blog', { method: 'POST', body: data });
  }
  
  static async updateBlogPost(id, data) {
    return this.request(`/blog/${id}`, { method: 'PUT', body: data });
  }
  
  static async deleteBlogPost(id) {
    return this.request(`/blog/${id}`, { method: 'DELETE' });
  }
  
  // Messages
  static async getMessages() {
    return this.request('/messages');
  }
  
  static async sendMessage(data) {
    return this.request('/messages', { method: 'POST', body: data });
  }
  
  static async markMessageRead(id) {
    return this.request(`/messages/${id}/read`, { method: 'PUT' });
  }
  
  static async deleteMessage(id) {
    return this.request(`/messages/${id}`, { method: 'DELETE' });
  }
  
  // Upload
  static async uploadImage(file, folder = 'nextgen-dev') {
    const formData = new FormData();
    formData.append('image', file);
    formData.append('folder', folder);
    
    return this.request('/upload', {
      method: 'POST',
      body: formData,
      headers: {} // Let browser set content-type
    });
  }
  
  // Stats
  static async getStats() {
    return this.request('/stats');
  }
  
  // Settings
  static async getSettings() {
    return this.request('/settings');
  }
  
  static async updateSettings(data) {
    return this.request('/settings', { method: 'PUT', body: data });
  }
}

// Make API available globally
window.API = API;
