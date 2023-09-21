import type { NextApiRequest, NextApiResponse } from "next";
import axios from "axios";
import { PriceByDateDataProps } from "../../../types";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<PriceByDateDataProps[] | { message: string }>
) {
  const { search_id } = req.query;
  const apiUrl = process.env.NEXT_PUBLIC_API_KEY as string;
  try {
    const response = await axios.get(`${apiUrl}/price-by-date`, {
      params: {
        search_id: search_id,
      },
    });
    res.status(200).json(response.data);
  } catch (error: unknown) {
    if (error instanceof Error) {
      res.status(500).json({
        message: error.message,
      });
    } else {
      res.status(500).json({
        message: "An unexpected error occurred.",
      });
    }
  }
}
