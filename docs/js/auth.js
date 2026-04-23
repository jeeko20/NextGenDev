// ========================================
// NextGen Dev - Authentication
// ========================================

class Auth {
  static _safeStorageGet(key) {
    try {
      return localStorage.getItem(key);
    } catch (error) {
      console.warn('LocalStorage inaccessible:', error);
      return null;
    }
  }

  static _safeStorageSet(key, value) {
    try {
      localStorage.setItem(key, value);
    } catch (error) {
      console.warn('LocalStorage inaccessible:', error);
    }
  }

  static _safeStorageRemove(key) {
    try {
      localStorage.removeItem(key);
    } catch (error) {
      console.warn('LocalStorage inaccessible:', error);
    }
  }

  static getToken() {
    return this._safeStorageGet('access_token');
  }
  
  static setToken(token) {
    this._safeStorageSet('access_token', token);
  }
  
  static removeToken() {
    this._safeStorageRemove('access_token');
    this._safeStorageRemove('user');
  }
  
  static getUser() {
    const user = this._safeStorageGet('user');
    return user ? JSON.parse(user) : null;
  }
  
  static setUser(user) {
    this._safeStorageSet('user', JSON.stringify(user));
  }
  
  static isAuthenticated() {
    return !!this.getToken();
  }
  
  static async login(username, password) {
    const data = await API.login(username, password);
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
