export class LoginModel {
    constructor(public email: string, public password: string) { }
}
export class LoginErrorsModel {
    constructor(public email: [], public password: []) { }
}