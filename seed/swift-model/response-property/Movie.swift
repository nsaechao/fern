//
//  Movie.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct Movie: Codable {

    enum CodingKeys: String, CodingKey {
        case id = "id"
        case name = "name"
    }

    public let id: String
    public let name: String

}
