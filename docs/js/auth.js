// ========================================
// NextGen Dev - Authentication
// ========================================

class Auth {
  static getToken() {
    return localStorage.getItem('access_token');
  }
  
  static setToken(token) {
    localStorage.setItem('access_token', token);
  }
  
  static removeToken() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
  }
  
  static getUser() {
    const user = localStorage.getItem('user');
    return user ? JSON.parse(user) : null;
  }
  
  static setUser(user) {
    localStorage.setItem('user', JSON.stringify(user));
  }
  
  static isAuthenticated() {
    return !!this.getToken();
  }
  
  static async login(email, password) {
    const data = await API.login(email, password);
    this.setToken(data.access_token);
    this.setUser(data.user);
    return data;
  }
  
  static async register(email, password, name) {
    return API.register(email, password, name);
  }
  
  static logout() {
    this.removeToken();
    window.location.href = '/';
  }
  
  static async checkAuth() {
    try {
      const data = await API.getMe();
      this.setUser(data.user);
      return true;
    } catch {
      this.removeToken();
      return false;
    }
  }
  
  static requireAuth() {
    if (!this.isAuthenticated()) {
      window.location.href = '/login.html';
      return false;
    }
    return true;
  }
  
  static updateUI() {
    const user = this.getUser();
    const authLinks = document.querySelectorAll('.auth-dependent');
    
    authLinks.forEach(el => {
      if (user) {
        el.style.display = '';
        if (el.dataset.authenticated) {
          el.style.display = el.dataset.authenticated;
        }
      } else {
        el.style.display = 'none';
        if (el.dataset.unauthenticated) {
          el.style.display = el.dataset.unauthenticated;
        }
      }
    });
  }
}

window.Auth = Auth;
